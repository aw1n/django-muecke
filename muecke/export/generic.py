# python imports
import csv

# django imports
from django.http import HttpResponse

# muecke imports
from muecke.export.utils import register
from muecke.export.models import Export


def export(request, export):
    """Generic export method.
    """
    response = HttpResponse(mimetype="text/csv")
    response["Content-Disposition"] = "attachment; filename=%s.csv" % export.name
    writer = csv.writer(response, delimiter=";", quotechar='"', quoting=csv.QUOTE_ALL)

    for product in export.get_products():
        writer.writerow((
            product.get_name().encode("utf-8"),
        ))
    return response
