# django imports
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.http import require_POST

# muecke imports
import muecke.core.utils
from muecke.catalog.models import Product
from muecke.tax.models import Tax
from muecke.manage.product_taxes.forms import TaxAddForm
from muecke.manage.product_taxes.forms import TaxForm


@permission_required("core.manage_shop", login_url="/login/")
def manage_taxes(request):
    """Dispatches to the first tax or to the add tax form.
    """
    try:
        tax = Tax.objects.all()[0]
        url = reverse("muecke_manage_tax", kwargs={"id": tax.id})
    except IndexError:
        url = reverse("muecke_manage_no_taxes")

    return HttpResponseRedirect(url)


@permission_required("core.manage_shop", login_url="/login/")
def manage_tax(request, id, template_name="manage/product_taxes/tax.html"):
    """Displays the main form to manage taxes.
    """
    tax = get_object_or_404(Tax, pk=id)
    if request.method == "POST":
        form = TaxForm(instance=tax, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return muecke.core.utils.set_message_cookie(
                url=reverse("muecke_manage_tax", kwargs={"id": tax.id}),
                msg=_(u"Tax has been saved."),
            )
    else:
        form = TaxForm(instance=tax)

    return render_to_response(template_name, RequestContext(request, {
        "tax": tax,
        "taxes": Tax.objects.all(),
        "form": form,
        "current_id": int(id),
    }))


@permission_required("core.manage_shop", login_url="/login/")
def no_taxes(request, template_name="manage/product_taxes/no_taxes.html"):
    """Displays that there are no taxes.
    """
    return render_to_response(template_name, RequestContext(request, {}))


@permission_required("core.manage_shop", login_url="/login/")
def add_tax(request, template_name="manage/product_taxes/add_tax.html"):
    """Provides a form to add a new tax.
    """
    if request.method == "POST":
        form = TaxAddForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            tax = form.save()

            return muecke.core.utils.set_message_cookie(
                url=reverse("muecke_manage_tax", kwargs={"id": tax.id}),
                msg=_(u"Tax has been added."),
            )
    else:
        form = TaxAddForm()

    return render_to_response(template_name, RequestContext(request, {
        "form": form,
        "taxes": Tax.objects.all(),
        "next": request.REQUEST.get("next", request.META.get("HTTP_REFERER")),
    }))


@permission_required("core.manage_shop", login_url="/login/")
@require_POST
def delete_tax(request, id):
    """Deletes tax with passed id.
    """
    tax = get_object_or_404(Tax, pk=id)

    # First remove the tax from all products.
    for product in Product.objects.filter(tax=id):
        product.tax = None
        product.save()

    tax.delete()

    return muecke.core.utils.set_message_cookie(
        url=reverse("muecke_manage_taxes"),
        msg=_(u"Tax has been deleted."),
    )
