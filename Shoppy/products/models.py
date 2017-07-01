from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=140)
    category = models.CharField(max_length=140)
    price = models.FloatField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
