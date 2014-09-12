# django imports
from django.contrib import admin

# muecke imports
from muecke.customer.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    """
    """
admin.site.register(Customer, CustomerAdmin)
