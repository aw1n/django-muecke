===
API
===

Plug-ins
========

.. _order_number_generator:

OrderNumberGenerator
--------------------

.. autoclass:: muecke.plugins.OrderNumberGenerator

    .. automethod:: muecke.plugins.OrderNumberGenerator.exclude_form_fields

    .. automethod:: muecke.plugins.OrderNumberGenerator.get_next

    .. automethod:: muecke.plugins.OrderNumberGenerator.get_form

.. _payment_method_proccessor:

PaymentMethodProcessor
----------------------

.. autoclass:: muecke.plugins.PaymentMethodProcessor

    .. automethod:: muecke.plugins.PaymentMethodProcessor.get_create_order_time

    .. automethod:: muecke.plugins.PaymentMethodProcessor.get_pay_link

    .. automethod:: muecke.plugins.PaymentMethodProcessor.process


.. _price_calculator:

PriceCalculator
---------------

.. autoclass:: muecke.plugins.PriceCalculator

    .. automethod:: muecke.plugins.PriceCalculator.get_price

    .. automethod:: muecke.plugins.PriceCalculator.get_price_net

    .. automethod:: muecke.plugins.PriceCalculator.get_price_gross

    .. automethod:: muecke.plugins.PriceCalculator.get_standard_price

    .. automethod:: muecke.plugins.PriceCalculator.get_standard_price_net

    .. automethod:: muecke.plugins.PriceCalculator.get_standard_price_gross

    .. automethod:: muecke.plugins.PriceCalculator.get_for_sale_price

    .. automethod:: muecke.plugins.PriceCalculator.get_for_sale_price_net

    .. automethod:: muecke.plugins.PriceCalculator.get_for_sale_price_gross

    .. automethod:: muecke.plugins.PriceCalculator.get_customer_tax_rate

    .. automethod:: muecke.plugins.PriceCalculator.get_customer_tax

    .. automethod:: muecke.plugins.PriceCalculator.get_product_tax_rate

    .. automethod:: muecke.plugins.PriceCalculator.get_product_tax

    .. automethod:: muecke.plugins.PriceCalculator.price_includes_tax

.. _shipping_method_price_calculator:

ShippingMethodPriceCalculator
-----------------------------

.. autoclass:: muecke.plugins.ShippingMethodPriceCalculator

    .. automethod:: muecke.plugins.ShippingMethodPriceCalculator.get_price_net

    .. automethod:: muecke.plugins.ShippingMethodPriceCalculator.get_price_gross

    .. automethod:: muecke.plugins.ShippingMethodPriceCalculator.get_tax
