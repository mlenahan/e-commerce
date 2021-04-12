import datetime
import decimal
import random

from faker import Faker

from products.base import Languages, ProductType, Rarity, Condition
from products.models import Product, ProductItem

fake = Faker()


def word_name(min_words=1, max_words=4):
    num_words = random.randint(min_words, max_words)
    return ' '.join(fake.words(num_words)).title()


def fake_description(min_num_words=50, max_num_words=100):
    words = random.randint(min_num_words, max_num_words)
    return fake.paragraph(words)


def fake_price(min_range=500, max_range=20000):
    return decimal.Decimal(random.randrange(min_range, max_range)) / 100


def fake_date(after=datetime.datetime(2021, 3, 8), before=datetime.datetime(2021, 5, 8)):

    time_between_dates = before - after
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return after + datetime.timedelta(days=random_number_of_days)


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
        description=fake_description(),
        price=fake_price(),
    )
    product.created_at = fake_date()
    product.save()
    return product


def fake_product_item(product):
    return ProductItem.objects.create(product=product, condition=choice_from_choice_class(Condition))
