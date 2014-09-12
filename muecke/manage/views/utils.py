# django imports
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django import forms

# muecke imports
import muecke.caching.utils
import muecke.core.utils
import muecke.catalog.models
import muecke.marketing.utils


@permission_required("core.manage_shop", login_url="/login/")
def utilities(request, template_name="manage/utils.html"):
    """Displays the utility view.
    """
    return render_to_response(template_name, RequestContext(request, {}))


@permission_required("core.manage_shop", login_url="/login/")
def reindex_topseller(request):
    """Clears and reindexes the topsellers.
    """
    muecke.marketing.utils.calculate_product_sales()
    return muecke.core.utils.set_message_cookie(
        url=reverse("muecke_manage_utils"),
        msg=_(u"Topseller have been reindexed."),
    )


@permission_required("core.manage_shop", login_url="/login/")
def clear_cache(request):
    """Clears the whole cache.
    """
    muecke.caching.utils.clear_cache()
    return muecke.core.utils.set_message_cookie(
        url=reverse("muecke_manage_utils"),
        msg=_(u"Cache has been cleared."),
    )


@permission_required("core.manage_shop", login_url="/login/")
def set_category_levels(request):
    """Sets the category levels based on the position in category hierarchy.
    """
    muecke.core.utils.set_category_levels()
    return muecke.core.utils.set_message_cookie(
        url=reverse("muecke_manage_utils"),
        msg=_(u"Category levels have been created."),
    )


@permission_required("core.manage_shop", login_url="/login/")
def update_effective_price(request):
    """Saves the price or sale price to effective price.
    """
    for product in muecke.catalog.models.Product.objects.all():
        product.save()

    return muecke.core.utils.set_message_cookie(
        url=reverse("muecke_manage_utils"),
        msg=_(u"Effective prices have been set."),
    )
