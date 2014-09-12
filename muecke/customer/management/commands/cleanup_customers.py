from django.core.management.base import BaseCommand


class Command(BaseCommand):
    args = ''
    help = 'Remove unregistered customers without carts and orders'

    def handle(self, *args, **options):
        from muecke.customer.models import Customer
        from muecke.order.models import Order
        from muecke.cart.models import Cart
        cnt = 0
        for customer in Customer.objects.filter(user__isnull=True):
            has_cart = Cart.objects.filter(session=customer.session).exists()
            has_orders = Order.objects.filter(session=customer.session).exists()
            if not has_cart and not has_orders:
                for address in customer.addresses.all():
                    if not address.order:
                        address.delete()
                customer.delete()
                cnt += 1
        print "Removed %s customers" % cnt
