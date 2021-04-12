import random

from django.core.management.base import BaseCommand
from products.utils.fixtures import fake_product, fake_product_item


class Command(BaseCommand):
    help = 'Generate random product'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of products to be created')

    def handle(self, *args, **kwargs):

        count = kwargs['count']

        for i in range(count):

            product = fake_product()

            self.stdout.write(str(product))
            self.stdout.write(str(product.created_at))
            for j in range(random.randrange(1, 10)):
                product_item = fake_product_item(product)
                self.stdout.write(str(product_item))
