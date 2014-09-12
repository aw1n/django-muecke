# django imports
from django.core.management.base import BaseCommand

from muecke.utils import generator


class Command(BaseCommand):
    args = ''
    help = 'Generates mock products for LFS'

    def handle(self, *args, **options):
        generator.products(20)
