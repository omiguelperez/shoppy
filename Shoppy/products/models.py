from django.db import models

from customers.models import Customer


class Product(models.Model):
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=140)
    category = models.CharField(max_length=140)
    price = models.FloatField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    product = models.ForeignKey(Product)
    customer = models.ForeignKey(Customer)
