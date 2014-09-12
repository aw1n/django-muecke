# django imports
from django.forms import ModelForm

# muecke imports
from muecke.discounts.models import Discount


class DiscountForm(ModelForm):
    """
    Form to manage discount data.
    """
    class Meta:
        model = Discount
