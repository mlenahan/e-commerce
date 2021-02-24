from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    rarity = models.CharField(default=None, blank=True, null=True, max_length=255)


class ProductItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    condition = models.CharField(max_length=255)

