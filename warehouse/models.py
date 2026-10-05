from django.db import models


# Create your models here.
class Sports_equipment(models.Model):
    name = models.CharField(max_length=48)
    category = models.CharField(max_length=48)
    material = models.CharField(max_length=48)
    brand = models.CharField(max_length=48)
    price = models.DecimalField(max_digits=6, decimal_places=2)
