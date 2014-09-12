# django imports
from django.forms import ModelForm

# muecke imports
from muecke.manufacturer.models import Manufacturer


class ManufacturerDataForm(ModelForm):
    """Form to manage selection data.
    """
    class Meta:
        model = Manufacturer
