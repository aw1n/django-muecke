# django imports
from django.forms import ModelForm

# muecke imports
from muecke.tax.models import Tax


class TaxForm(ModelForm):
    """Form to edit a tax.
    """
    class Meta:
        model = Tax


class TaxAddForm(ModelForm):
    """Form to add a tax.
    """
    class Meta:
        model = Tax
        fields = ("rate", )
