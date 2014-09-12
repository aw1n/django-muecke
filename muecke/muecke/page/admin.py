# django imports
from django.contrib import admin

# muecke imports
from muecke.page.models import Page


class PageAdmin(admin.ModelAdmin):
    """
    """
admin.site.register(Page, PageAdmin)
