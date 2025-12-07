from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class restaurant(models.Model):
    id_restaurant = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    stars = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    tables = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.name