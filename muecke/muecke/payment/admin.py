# django imports
from django.contrib import admin

# muecke imports
from muecke.payment.models import PaymentMethod
from muecke.payment.models import PaymentMethodPrice
from muecke.payment.models import PayPalOrderTransaction


class PaymentMethodAdmin(admin.ModelAdmin):
    """
    """
admin.site.register(PaymentMethod, PaymentMethodAdmin)


class PaymentMethodPriceAdmin(admin.ModelAdmin):
    """
    """
admin.site.register(PaymentMethodPrice, PaymentMethodPriceAdmin)


class PayPalOrderTransactionAdmin(admin.ModelAdmin):
    """
    """
admin.site.register(PayPalOrderTransaction, PayPalOrderTransactionAdmin)
