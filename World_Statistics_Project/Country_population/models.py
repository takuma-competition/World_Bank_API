from django.db import models


class Population(models.Model):
    year = models.IntegerField(default=0)
    population = models.FloatField()


# Create your models here.
