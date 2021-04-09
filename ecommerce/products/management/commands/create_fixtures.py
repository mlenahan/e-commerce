import random

from django.core.management.base import BaseCommand
from products.utils.fixtures import word_name, fake_description, fake_price,\
    fake_date, \
    choice_from_choice_class, fake_product, fake_product_item

class Command(BaseCommand):
    help = 'Generate random product'

    def add_arguments(self, parser):
            parser.add_argument('count', type=int, help='Indicates the number of products to be created')

    def handle(self, *args, **kwargs):

        count = kwargs['count']

        for i in range(count):

            product = fake_product()

            print(product)
            print(product.created_at)


            for x in range(random.randrange(1, 10)):
                product_item = fake_product_item(product)
                print(product_item)