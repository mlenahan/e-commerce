from django.db import models
from products.base import Rarity, Languages, Condition, ProductType

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255, choices=ProductType.CHOICES)
    language = models.CharField(max_length=255, choices=Languages.CHOICES)
    rarity = models.CharField(blank=True, null=True, max_length=255, choices=Rarity.CHOICES)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    description = models.TextField(max_length=None)

    def __str__(self):
        return self.name


class ProductItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    condition = models.CharField(max_length=255, choices=Condition.CHOICES)
