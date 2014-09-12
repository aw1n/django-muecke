# django imports
from django.contrib import admin

# muecke imports
from muecke.marketing.models import Topseller, FeaturedProduct

admin.site.register(Topseller)
admin.site.register(FeaturedProduct)
