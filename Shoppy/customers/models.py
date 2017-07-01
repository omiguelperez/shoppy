from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=140)
    email = models.EmailField(max_length=140)
    phone = models.IntegerField(unique=True)
    address = models.CharField(max_length=140)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name
