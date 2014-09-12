# django imports
from django.forms import ModelForm

# muecke imports
from muecke.catalog.models import PropertyGroup


class PropertyGroupForm(ModelForm):
    """
    Form to add/edit a property group.
    """
    class Meta:
        model = PropertyGroup
        fields = ["name"]
