# django imports
from django.contrib import admin

# muecke imports
from muecke.catalog.models import Category
from muecke.catalog.models import FilterStep
from muecke.catalog.models import Image
from muecke.catalog.models import Product
from muecke.catalog.models import ProductAccessories
from muecke.catalog.models import Property
from muecke.catalog.models import PropertyOption
from muecke.catalog.models import PropertyGroup
from muecke.catalog.models import ProductPropertyValue
from muecke.catalog.models import StaticBlock
from muecke.catalog.models import DeliveryTime


class CategoryAdmin(admin.ModelAdmin):
    """
    """
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
admin.site.register(Product, ProductAdmin)


class ImageAdmin(admin.ModelAdmin):
    """
    """
admin.site.register(Image, ImageAdmin)


class ProductAccessoriesAdmin(admin.ModelAdmin):
    """
    """
admin.site.register(ProductAccessories, ProductAccessoriesAdmin)


class StaticBlockAdmin(admin.ModelAdmin):
    """
    """
admin.site.register(StaticBlock, StaticBlockAdmin)


class DeliveryTimeAdmin(admin.ModelAdmin):
    """
    """
admin.site.register(DeliveryTime, DeliveryTimeAdmin)


admin.site.register(PropertyGroup)
admin.site.register(Property)
admin.site.register(PropertyOption)
admin.site.register(ProductPropertyValue)
admin.site.register(FilterStep)
