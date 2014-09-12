# muecke imports
from muecke.plugins import ShippingMethodPriceCalculator


class GrossShippingMethodPriceCalculator(ShippingMethodPriceCalculator):
    """
    ShippingMethodPriceCalculator which considers the entered price as gross
    price.

    See muecke.plugins.ShippingMethodPriceCalculator
    """
    def get_price_net(self):
        """See muecke.plugins.ShippingMethodPriceCalculator.
        """
        try:
            return self.shipping_method.price / ((100 + self.shipping_method.tax.rate) / 100)
        except AttributeError:
            return self.shipping_method.price

    def get_price_gross(self):
        """See muecke.plugins.ShippingMethodPriceCalculator.
        """
        return self.shipping_method.price


class NetShippingMethodPriceCalculator(ShippingMethodPriceCalculator):
    """
    ShippingMethodPriceCalculator which considers the entered price as net
    price.
    """
    def get_price_net(self):
        """See muecke.plugins.ShippingMethodPriceCalculator.
        """
        return self.shipping_method.price

    def get_price_gross(self):
        """See muecke.plugins.ShippingMethodPriceCalculator.
        """
        try:
            return self.shipping_method.price * ((100 + self.shipping_method.tax.rate) / 100)
        except AttributeError:
            return self.shipping_method.price
