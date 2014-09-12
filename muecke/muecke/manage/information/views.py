import json

# django imports
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render_to_response
from django.template import RequestContext

# muecke imports
from muecke.core.utils import import_symbol

# versions
from muecke import __version__ as muecke_version
from muecke_theme import __version__ as muecke_theme_version

@permission_required("core.manage_shop")
def environment(request, template_name="manage/information/environment.html"):
    """Displays miscellaneous information about the evnironment.
    """
    apps = []
    for app in settings.INSTALLED_APPS:
        if app in ["muecke"] or \
           app.startswith("muecke.") or \
           app.startswith("django."):
            continue

        try:
            version = import_symbol("%s.__version__" % app)
        except AttributeError:
            version = "N/A"

        apps.append({
            "name": app,
            "version": version,
        })

    apps.sort(lambda a, b: cmp(a["name"], b["name"]))

    return render_to_response(template_name, RequestContext(request, {
        "muecke_version": muecke_version,
        "muecke_theme_version": muecke_theme_version,
        "apps": apps,
    }))
