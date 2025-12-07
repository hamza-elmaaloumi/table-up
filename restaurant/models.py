from django.db import models

# Create your models here.
class restaurant(models.Model):
    id_restaurant = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    stars = models.IntegerField(max_length=256)
    tables = models.IntegerField(max_length=256)
    capacity = models.Integer