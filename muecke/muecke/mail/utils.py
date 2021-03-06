# django imports
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.template.base import TemplateDoesNotExist
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _


def send_order_sent_mail(order):
    """Sends an order has been sent mail to the shop customer
    """
    import muecke.core.utils
    shop = muecke.core.utils.get_default_shop()

    try:
        subject = render_to_string("muecke/mail/order_sent_subject.txt", {"order": order})
    except TemplateDoesNotExist:
        subject = _(u"Your order has been sent")

    from_email = shop.from_email
    to = [order.customer_email]
    bcc = shop.get_notification_emails()

    # text
    text = render_to_string("muecke/mail/order_sent_mail.txt", {"order": order})
    mail = EmailMultiAlternatives(
        subject=subject, body=text, from_email=from_email, to=to, bcc=bcc)

    # html
    html = render_to_string("muecke/mail/order_sent_mail.html", {
        "order": order
    })

    mail.attach_alternative(html, "text/html")
    mail.send(fail_silently=True)


def send_order_paid_mail(order):
    """Sends an order has been paid mail to the shop customer.
    """
    import muecke.core.utils
    shop = muecke.core.utils.get_default_shop()

    try:
        subject = render_to_string("muecke/mail/order_paid_subject.txt", {"order": order})
    except TemplateDoesNotExist:
        subject = _(u"Your order has been paid")

    from_email = shop.from_email
    to = [order.customer_email]
    bcc = shop.get_notification_emails()

    # text
    text = render_to_string("muecke/mail/order_paid_mail.txt", {"order": order})
    mail = EmailMultiAlternatives(
        subject=subject, body=text, from_email=from_email, to=to, bcc=bcc)

    # html
    html = render_to_string("muecke/mail/order_paid_mail.html", {
        "order": order
    })

    mail.attach_alternative(html, "text/html")
    mail.send(fail_silently=True)


def send_order_received_mail(order):
    """Sends an order received mail to the shop customer.

    Customer information is taken from the provided order.
    """
    import muecke.core.utils
    shop = muecke.core.utils.get_default_shop()

    try:
        subject = render_to_string("muecke/mail/order_received_subject.txt", {"order": order})
    except TemplateDoesNotExist:
        subject = _(u"Your order has been received")

    from_email = shop.from_email
    to = [order.customer_email]
    bcc = shop.get_notification_emails()

    # text
    text = render_to_string("muecke/mail/order_received_mail.txt", {"order": order})
    mail = EmailMultiAlternatives(
        subject=subject, body=text, from_email=from_email, to=to, bcc=bcc)

    # html
    html = render_to_string("muecke/mail/order_received_mail.html", {
        "order": order
    })

    mail.attach_alternative(html, "text/html")
    mail.send(fail_silently=True)


def send_customer_added(user):
    """Sends a mail to a newly registered user.
    """
    import muecke.core.utils
    shop = muecke.core.utils.get_default_shop()
    subject = _(u"Welcome to %s" % shop.name)

    from_email = shop.from_email
    to = [user.username]
    bcc = shop.get_notification_emails()

    # text
    text = render_to_string("muecke/mail/new_user_mail.txt", {
        "user": user, "shop": shop})

    # subject
    subject = render_to_string("muecke/mail/new_user_mail_subject.txt", {
        "user": user, "shop": shop})

    mail = EmailMultiAlternatives(
        subject=subject, body=text, from_email=from_email, to=to, bcc=bcc)

    # html
    html = render_to_string("muecke/mail/new_user_mail.html", {
        "user": user, "shop": shop,
    })

    mail.attach_alternative(html, "text/html")
    mail.send(fail_silently=True)


def send_review_added(review):
    """Sends a mail to shop admins that a new review has been added
    """
    import muecke.core.utils
    shop = muecke.core.utils.get_default_shop()

    subject = _(u"New review has been added")
    from_email = shop.from_email
    to = shop.get_notification_emails()

    ctype = ContentType.objects.get_for_id(review.content_type_id)
    product = ctype.get_object_for_this_type(pk=review.content_id)

    # text
    text = render_to_string("muecke/mail/review_added_mail.txt", {
        "review": review,
        "product": product,
    })

    mail = EmailMultiAlternatives(
        subject=subject, body=text, from_email=from_email, to=to)

    # html
    html = render_to_string("muecke/mail/review_added_mail.html", {
        "site": "http://%s" % Site.objects.get(id=settings.SITE_ID),
        "review": review,
        "product": product,
    })

    mail.attach_alternative(html, "text/html")
    mail.send(fail_silently=True)
