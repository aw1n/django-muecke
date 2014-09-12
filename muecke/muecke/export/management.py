# django imports
from django.db.models.signals import post_syncdb

# muecke imports
from muecke.export.utils import register
from muecke.export.generic import export as export_script
from muecke.export.models import Script
import muecke


def register_muecke_scripts(sender, **kwargs):
    # don't register our scripts until the table has been created by syncdb
    if sender == muecke.export.models:
        register(export_script, "Generic")
post_syncdb.connect(register_muecke_scripts)
