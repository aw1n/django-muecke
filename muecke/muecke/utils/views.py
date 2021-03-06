# python imports
import os
import csv

# django imports
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.base import ContentFile
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.defaultfilters import slugify

# django imports
from django.http import HttpResponse

# muecke imports
from muecke.catalog.models import Category
from muecke.catalog.models import Product
from muecke.catalog.models import ProductAccessories
from muecke.catalog.models import Image


def test(request):
    """
    """
    return render_to_response("test.html", RequestContext(request))


def upload_test(request):
    """
    """
    if request.method == "GET":
        return render_to_response("testuploadform.html")

    return HttpResponse()
