# django imports
from django import forms
from django.db import models
from django.template import RequestContext
from django.template.loader import render_to_string

# portlets imports
from portlets.models import Portlet

# muecke imports
import muecke.catalog.utils
import muecke.catalog.models
import muecke.marketing.utils


class TopsellerPortlet(Portlet):
    """Portlet to display recent visited products.
    """
    limit = models.IntegerField(default=5)

    class Meta:
        app_label = 'portlet'

    def __unicode__(self):
        return "%s" % self.id

    def render(self, context):
        """Renders the portlet as html.
        """
        request = context.get("request")
        object = context.get("category") or context.get("product")
        if object is None:
            topseller = muecke.marketing.utils.get_topseller(self.limit)
        elif isinstance(object, muecke.catalog.models.Product):
            category = object.get_current_category(context.get("request"))
            topseller = muecke.marketing.utils.get_topseller_for_category(
                category, self.limit)
        else:
            topseller = muecke.marketing.utils.get_topseller_for_category(
                object, self.limit)

        return render_to_string("muecke/portlets/topseller.html", RequestContext(request, {
            "title": self.title,
            "topseller": topseller,
        }))

    def form(self, **kwargs):
        return TopsellerForm(instance=self, **kwargs)


class TopsellerForm(forms.ModelForm):
    """Form for the TopsellerPortlet.
    """
    class Meta:
        model = TopsellerPortlet
