# django imports
from django.contrib import admin

# muecke imports
from muecke.criteria.models.criteria_objects import CriteriaObjects
from muecke.criteria.models.criteria import CartPriceCriterion
from muecke.criteria.models.criteria import WeightCriterion
from muecke.criteria.models.criteria import CountryCriterion


class CartPriceCriterionAdmin(admin.ModelAdmin):
    """
    """
admin.site.register(CartPriceCriterion, CartPriceCriterionAdmin)


class CountryCriterionAdmin(admin.ModelAdmin):
    """
    """
admin.site.register(CountryCriterion, CountryCriterionAdmin)


class WeightCriterionAdmin(admin.ModelAdmin):
    """
    """
admin.site.register(WeightCriterion, WeightCriterionAdmin)


class CriteriaObjectsAdmin(admin.ModelAdmin):
    """
    """
admin.site.register(CriteriaObjects, CriteriaObjectsAdmin)
