# django imports
from django.contrib import admin

# muecke imports
from muecke.core.models import Action
from muecke.core.models import ActionGroup
from muecke.core.models import Shop
from muecke.core.models import Country

admin.site.register(Shop)
admin.site.register(Action)
admin.site.register(ActionGroup)
admin.site.register(Country)
