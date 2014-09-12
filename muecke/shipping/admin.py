# django imports
from django.contrib import admin

# muecke imports
from muecke.shipping.models import ShippingMethod
from muecke.shipping.models import ShippingMethodPrice


class ShippingMethodAdmin(admin.ModelAdmin):
    """
    """
admin.site.register(ShippingMethod, ShippingMethodAdmin)


class ShippingMethodPriceAdmin(admin.ModelAdmin):
    """
    """
admin.site.register(ShippingMethodPrice, ShippingMethodPriceAdmin)
