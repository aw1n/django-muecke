# django imports
from django.conf.urls.defaults import *

# muecke imports
from muecke.catalog.models import Product

# tagging imports
from tagging.views import tagged_object_list

urlpatterns = patterns("muecke.tagging.views",
    url(r'tag-products/(?P<source>[^/]+)$', "tag_products", name="muecke_tag_products"),
    url(r'products/tag/(?P<tag>[^/]+)/$', tagged_object_list,
        dict(queryset_or_model=Product, paginate_by=10, allow_empty=True,
             template_name='tagging/product_list.html',
             template_object_name='product'), name='product_tag_detail'),
)
