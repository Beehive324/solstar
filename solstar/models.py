from django.db import models

class Produt(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField
    description = models.CharField(max_length=100)
     