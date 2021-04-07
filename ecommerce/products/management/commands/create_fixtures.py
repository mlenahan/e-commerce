import random

from django.core.management.base import BaseCommand
from faker import Faker

from products.models import Product
from products.base import Languages, ProductType, Rarity


fake = Faker()


def word_name():
    num_words = random.randint(1, 4)
    return ' '.join(fake.words(num_words)).title()


def choice_from_choice_class(cls, nullable=False):
    choices = [c[0] for c in cls.CHOICES]
    if nullable:
        choices.append(None)
    return random.choice(choices)


def fake_product():
    # TODO add description
    # TODO add created_at - This should be edited after object is created
    # TODO add price - not sure how to get random decimal in range but should be able to google it.
    return Product.objects.create(
        name=word_name(),
        product_type=choice_from_choice_class(ProductType),
        language=choice_from_choice_class(Languages),
        rarity=choice_from_choice_class(Rarity, True),
    )


def fake_product_item(product):
    pass


class Command(BaseCommand):
    help = 'Generate random product'

    def add_arguments(self, parser):
            parser.add_argument('count', type=int, help='Indicates the number of products to be created')

    def handle(self, *args, **kwargs):

        count = kwargs['count']

        for i in range(count):
            product = fake_product()
            # TODO Create between 0 and 10 product items for each product
            # for i in range(random_number_of_products):
            #     fake_product_item(product)
            print(product)

