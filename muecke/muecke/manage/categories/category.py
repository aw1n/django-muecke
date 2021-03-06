# django imports
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.utils import simplejson
from django.utils.translation import ugettext_lazy as _

# muecke imports
from muecke.caching.utils import muecke_get_object_or_404
from muecke.catalog.models import Category
from muecke.core.utils import LazyEncoder
from muecke.core.utils import set_category_levels
from muecke.core.widgets.image import LFSImageInput
from muecke.manage import utils as manage_utils
from muecke.manage.categories.products import manage_products
from muecke.manage.categories.seo import edit_seo
from muecke.manage.categories.view import category_view
from muecke.manage.categories.portlet import manage_categories_portlet
from muecke.manage.views.muecke_portlets import portlets_inline


class CategoryAddForm(ModelForm):
    """Process form to add a category.
    """
    class Meta:
        model = Category
        fields = ("name", "slug")


class CategoryForm(ModelForm):
    """Process form to edit a category.
    """
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields["image"].widget = LFSImageInput()

        try:
            context = kwargs["instance"]
        except KeyError:
            context = None

    class Meta:
        model = Category
        fields = ("name", "slug", "short_description", "description", "short_description",
        "exclude_from_navigation", "image", "static_block")


@permission_required("core.manage_shop", login_url="/login/")
def manage_categories(request):
    """Dispatches to the first category or to the add category form if no
    category exists yet.
    """
    try:
        category = Category.objects.all()[0]
    except IndexError:
        url = reverse("muecke_manage_no_categories")
    else:
        url = reverse("muecke_manage_category", kwargs={"category_id": category.id})

    return HttpResponseRedirect(url)


@permission_required("core.manage_shop", login_url="/login/")
def manage_category(request, category_id, template_name="manage/category/manage_category.html"):
    """Displays the form to manage the category with given category id.
    """
    category = Category.objects.get(pk=category_id)

    return render_to_response(template_name, RequestContext(request, {
        "categories_portlet": manage_categories_portlet(request, category_id),
        "category": category,
        "data": category_data(request, category_id),
        "seo": edit_seo(request, category_id),
        "view": category_view(request, category_id),
        "portlets": portlets_inline(request, category),
        "dialog_message": _("Do you really want to delete the category <b>'%(name)s'</b> and all its sub categories?") % {"name": category.name},
    }))


@permission_required("core.manage_shop", login_url="/login/")
def category_data(request, category_id, form=None, template_name="manage/category/data.html"):
    """Displays the core data for the category_id with passed category_id.

    This is used as a part of the whole category form.
    """
    category = Category.objects.get(pk=category_id)

    if request.method == "POST":
        form = CategoryForm(instance=category, data=request.POST)
    else:
        form = CategoryForm(instance=category)

    return render_to_string(template_name, RequestContext(request, {
        "category": category,
        "form": form,
    }))


@permission_required("core.manage_shop", login_url="/login/")
def category_by_id(request, category_id):
    """
    Little helper which returns a category by id. (For the shop customer the
    products are displayed by slug, for the manager by id).
    """
    category = Category.objects.get(pk=category_id)
    url = reverse("muecke.catalog.views.category_view", kwargs={"slug": category.slug})
    return HttpResponseRedirect(url)


# Actions
@permission_required("core.manage_shop", login_url="/login/")
def edit_category_data(request, category_id, template_name="manage/category/data.html"):
    """Updates the category data.
    """
    category = Category.objects.get(pk=category_id)

    form = CategoryForm(instance=category, data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        message = _(u"Category data have been saved.")
    else:
        message = _(u"Please correct the indicated errors.")

    # Delete image
    if request.POST.get("delete_image"):
        category.image.delete()

    html = [
        ["#data", category_data(request, category.id)],
        ["#categories-portlet", manage_categories_portlet(request, category.id)],
    ]

    result = simplejson.dumps({
        "message": message,
        "html" : html,
    }, cls=LazyEncoder)

    return HttpResponse(result)


@permission_required("core.manage_shop", login_url="/login/")
def add_category(request, category_id="", template_name="manage/category/add_category.html"):
    """Provides an add form and adds a new category to category with given id.
    """
    if category_id == "":
        parent = None
    else:
        try:
            parent = Category.objects.get(pk=category_id)
        except ObjectDoesNotExist:
            parent = None

    if request.method == "POST":
        form = CategoryAddForm(data=request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.parent = parent
            new_category.position = 999
            if parent:
                new_category.level = parent.level + 1
            new_category.save()

            # Update positions
            manage_utils.update_category_positions(parent)
            url = reverse("muecke_manage_category", kwargs={"category_id": new_category.id})
            return HttpResponseRedirect(url)
    else:
        form = CategoryAddForm(initial={"parent": category_id})

    return render_to_response(template_name, RequestContext(request, {
        "category": parent,
        "form": form,
        "came_from": request.REQUEST.get("came_from", reverse("muecke_manage_categories")),
    }))


@permission_required("core.manage_shop", login_url="/login/")
@require_POST
def delete_category(request, id):
    """Deletes category with given id.
    """
    category = muecke_get_object_or_404(Category, pk=id)
    parent = category.parent
    category.delete()
    manage_utils.update_category_positions(parent)

    url = reverse("muecke_manage_categories")
    return HttpResponseRedirect(url)


@permission_required("core.manage_shop", login_url="/login/")
def sort_categories(request):
    """Sort categories
    """
    category_list = request.POST.get("categories", "").split('&')
    assert (isinstance(category_list, list))
    if len(category_list) > 0:
        pos = 10
        for cat_str in category_list:
            child, parent_id = cat_str.split('=')
            child_id = child[9:-1]  # category[2]
            child_obj = Category.objects.get(pk=child_id)

            parent_obj = None
            if parent_id != 'root':
                parent_obj = Category.objects.get(pk=parent_id)

            child_obj.parent = parent_obj
            child_obj.position = pos
            child_obj.save()

            pos = pos + 10

    set_category_levels()

    result = simplejson.dumps({
        "message": _(u"The categories have been sorted."),
    }, cls=LazyEncoder)

    return HttpResponse(result)


# Privates
def _category_choices(context):
    """Returns categories to be used as choices for the field parent.
    Note: context is the category for which the form is applied.
    """
    categories = [("", "-")]
    for category in Category.objects.filter(parent=None):
        if context != category:
            categories.append((category.id, category.name))
            _category_choices_children(categories, category, context)
    return categories


def _category_choices_children(categories, category, context, level=1):
    """Adds the children of the given category to categories.
    Note: context is the category for which the form is applied.
    """
    for category in category.category_set.all():
        if context != category:
            categories.append((category.id, "%s %s" % ("-" * level * 5, category.name)))
            _category_choices_children(categories, category, context, level + 1)
