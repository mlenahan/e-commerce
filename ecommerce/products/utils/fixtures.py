import random
import decimal
import time
import datetime

from products.models import Product, ProductItem
from products.base import Languages, ProductType, Rarity, Condition

from faker import Faker

fake = Faker()

def word_name():
    num_words = random.randint(1, 4)
    return ' '.join(fake.words(num_words)).title()

def fake_description(min_num_words=50, max_num_words=100):
    words = random.randint(min_num_words, max_num_words)
    return fake.paragraph(words)

def fake_price():
    price = decimal.Decimal(random.randrange(500, 20000))/100
    return price

def fake_date(after=datetime.datetime(2021, 3, 8), before=datetime.datetime(2021, 5, 8)):

    time_between_dates = before - after
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = after + datetime.timedelta(days=random_number_of_days)

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
        description=fake_description(),
        price=fake_price(),
    )
    product.created_at = fake_date()
    product.save()
    return product


def fake_product_item(product):
    product_item = ProductItem.objects.create(product=product, condition=choice_from_choice_class(Condition))
    return product_item
