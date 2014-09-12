# django imports
from django.forms import ModelForm

# muecke imports
from muecke.catalog.models import StaticBlock


class StaticBlockForm(ModelForm):
    """
    Form to add and edit a static block.
    """
    class Meta:
        model = StaticBlock
        exclude = ("position", )
