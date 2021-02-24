from django.db import models
from core.models.base import (Rarity, Languages, Condition, ProductType)

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255, choices=ProductType.CHOICES)
    language = models.CharField(max_length=255, choices=Languages.CHOICES)
    rarity = models.CharField(blank=True, null=True, max_length=255, choices=Rarity.CHOICES)


class ProductItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    condition = models.CharField(max_length=255, choices=Condition.CHOICES)
