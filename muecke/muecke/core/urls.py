# django imports
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

# muecke imports
from muecke.core.sitemap import CategorySitemap
from muecke.core.sitemap import PageSitemap
from muecke.core.sitemap import ProductSitemap
from muecke.core.sitemap import ShopSitemap
from muecke.core.views import one_time_setup

# Robots
urlpatterns = patterns('django.views.generic.simple',
    (r'^robots.txt', 'direct_to_template', {'template': 'muecke/shop/robots.txt'}),
)

# Sitemaps
urlpatterns += patterns("django.contrib.sitemaps.views",
    url(r'^sitemap.xml$', 'sitemap', {'sitemaps': {"products": ProductSitemap, "categories": CategorySitemap, "pages": PageSitemap, "shop": ShopSitemap}})
)

# Shop
urlpatterns += patterns('muecke.core.views',
    url(r'^$', "shop_view", name="muecke_shop_view"),
)

# Cart
urlpatterns += patterns('muecke.cart.views',
    url(r'^add-to-cart$', "add_to_cart"),
    url(r'^add-accessory-to-cart/(?P<product_id>\d*)/(?P<quantity>.*)$', "add_accessory_to_cart", name="muecke_add_accessory_to_cart"),
    url(r'^added-to-cart$', "added_to_cart", name="muecke_added_to_cart"),
    url(r'^delete-cart-item/(?P<cart_item_id>\d*)$', "delete_cart_item", name="muecke_delete_cart_item"),
    url(r'^refresh-cart$', "refresh_cart"),
    url(r'^cart$', "cart", name="muecke_cart"),
    url(r'^check-voucher-cart/$', "check_voucher", name="muecke_check_voucher_cart"),
)

# Catalog
urlpatterns += patterns('muecke.catalog.views',
    url(r'^category-(?P<slug>[-\w]*)$', "category_view", name="muecke_category"),
    url(r'^product/(?P<slug>[-\w]*)$', "product_view", name="muecke_product"),
    url(r'^product-form-dispatcher', "product_form_dispatcher", name="muecke_product_dispatcher"),
    url(r'^set-sorting', "set_sorting", name="muecke_catalog_set_sorting"),
    url(r'^set-product-filter/(?P<category_slug>[-\w]+)/(?P<property_id>\d+)/(?P<min>.+)/(?P<max>.+)', "set_filter", name="muecke_set_product_filter"),
    url(r'^set-product-filter/(?P<category_slug>[-\w]+)/(?P<property_id>\d+)/(?P<value>.+)', "set_filter", name="muecke_set_product_filter"),
    url(r'^set-price-filter/(?P<category_slug>[-\w]+)/$', "set_price_filter", name="muecke_set_price_filter"),
    url(r'^reset-price-filter/(?P<category_slug>[-\w]+)/$', "reset_price_filter", name="muecke_reset_price_filter"),
    url(r'^reset-product-filter/(?P<category_slug>[-\w]+)/(?P<property_id>\d+)', "reset_filter", name="muecke_reset_product_filter"),
    url(r'^reset-all-product-filter/(?P<category_slug>[-\w]+)', "reset_all_filter", name="muecke_reset_all_product_filter"),
    url(r'^select-variant$', "select_variant", name="muecke_select_variant"),
    url(r'^select-variant-from-properties$', "select_variant_from_properties", name="muecke_select_variant_from_properties"),
    url(r'^file/(?P<id>[-\w]*)', "file", name="muecke_file"),
    url(r'^calculate-price/(?P<id>[-\w]*)', "calculate_price", name="muecke_calculate_price"),
    url(r'^calculate-packing/(?P<id>[-\w]*)', "calculate_packing", name="muecke_calculate_packing"),
)

# Checkout
urlpatterns += patterns('muecke.checkout.views',
    url(r'^checkout-dispatcher', "checkout_dispatcher", name="muecke_checkout_dispatcher"),
    url(r'^checkout-login', "login", name="muecke_checkout_login"),
    url(r'^checkout', "one_page_checkout", name="muecke_checkout"),
    url(r'^thank-you', "thank_you", name="muecke_thank_you"),
    url(r'^changed-checkout/$', "changed_checkout", name="muecke_changed_checkout"),
    url(r'^changed-invoice-country/$', "changed_invoice_country", name="muecke_changed_invoice_country"),
    url(r'^changed-shipping-country/$', "changed_shipping_country", name="muecke_changed_shipping_country"),
    url(r'^check-voucher/$', "check_voucher", name="muecke_check_voucher"),
)

# Customer
urlpatterns += patterns('muecke.customer.views',
    url(r'^login', "login", name="muecke_login"),
    url(r'^logout', "logout", name="muecke_logout"),
    url(r'^my-account', "account", name="muecke_my_account"),
    url(r'^my-addresses', "addresses", name="muecke_my_addresses"),
    url(r'^my-email', "email", name="muecke_my_email"),
    url(r'^my-orders', "orders", name="muecke_my_orders"),
    url(r'^my-order/(?P<id>\d+)', "order", name="muecke_my_order"),
    url(r'^my-password', "password", name="muecke_my_password"),
)

# Page
urlpatterns += patterns('muecke.page.views',
    url(r'^page/(?P<slug>[-\w]*)$', "page_view", name="muecke_page_view"),
    url(r'^pages/$', "pages_view", name="muecke_pages"),
    url(r'^popup/(?P<slug>[-\w]*)$', "popup_view", name="muecke_popup_view"),
)

# Password reset
urlpatterns += patterns('django.contrib.auth.views',
     url(r'^password-reset/$', "password_reset", name="muecke_password_reset"),
     url(r'^password-reset-done/$', "password_reset_done"),
     url(r'^password-reset-confirm/(?P<uidb36>[-\w]*)/(?P<token>[-\w]*)$', "password_reset_confirm"),
     url(r'^password-reset-complete/$', "password_reset_complete"),
)

# Search
urlpatterns += patterns('muecke.search.views',
    url(r'^search', "search", name="muecke_search"),
    url(r'^livesearch', "livesearch", name="muecke_livesearch"),
)

# Tagging
urlpatterns += patterns('',
    (r'^tagging/', include('muecke.tagging.urls')),
)

urlpatterns += patterns('',
    (r'', include('muecke_contact.urls')),
)


one_time_setup()
