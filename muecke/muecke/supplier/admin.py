# django imports
from django.contrib import admin

# muecke imports
from muecke.supplier.models import Supplier


class SupplierAdmin(admin.ModelAdmin):
    """
    """
admin.site.register(Supplier, SupplierAdmin)
