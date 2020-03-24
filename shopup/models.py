import datetime
from django.db import models
from django.utils import timezone


# Create your models here.

class Product(models.Model):
    sku = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    def days_published(self):
        return timezone.now() - self.pub_date
