# django imports
from django.forms import ModelForm

# muecke imports
from muecke.catalog.models import DeliveryTime


class DeliveryTimeAddForm(ModelForm):
    """Form to edit add a delivery time.
    """
    class Meta:
        model = DeliveryTime
        fields = ("min", "max", "unit")


class DeliveryTimeForm(ModelForm):
    """Form to edit a delivery time.
    """
    class Meta:
        model = DeliveryTime
