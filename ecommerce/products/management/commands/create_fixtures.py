from products.models import Product
from django.core.management.base import BaseCommand
from faker import Faker


fake = Faker()

class Command(BaseCommand):
    help = 'Generate random product'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of products to be created')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(count):
            Product.objects.create(name=fake.name())
            print(fake.name())

