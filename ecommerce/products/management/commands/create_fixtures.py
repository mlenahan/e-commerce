import random
import decimal
import time
import datetime

from django.core.management.base import BaseCommand
from faker import Faker

from products.models import Product, ProductItem
from products.base import Languages, ProductType, Rarity, Condition


fake = Faker()

def word_name():
    num_words = random.randint(1, 4)
    return ' '.join(fake.words(num_words)).title()

def random_description():
    desc = random.randint(50, 100)
    return fake.paragraph(desc)

def random_price():
    price = decimal.Decimal(random.randrange(500, 20000))/100
    return price

def product_created_at():
    start_date = datetime.datetime(2021, 3, 8)
    end_date = datetime.datetime(2021, 5, 8)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date

def choice_from_choice_class(cls, nullable=False):
    choices = [c[0] for c in cls.CHOICES]
    if nullable:
        choices.append(None)
    return random.choice(choices)


def fake_product():
    product = Product.objects.create(
        name=word_name(),
        product_type=choice_from_choice_class(ProductType),
        language=choice_from_choice_class(Languages),
        rarity=choice_from_choice_class(Rarity, True),
        description=random_description(),
        price=random_price(),
    )
    product.created_at = product_created_at()
    product.save()
    return product


def fake_product_item(product):
    product_item = ProductItem.objects.create(product=product, condition=choice_from_choice_class(Condition))
    return product_item


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

