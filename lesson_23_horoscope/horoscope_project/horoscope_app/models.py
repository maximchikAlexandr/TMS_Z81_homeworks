from django.db import models


# Create your models here.
class Zodiac(models.Model):
    latin_name = models.CharField(max_length=15)
    russian_name = models.CharField(max_length=15)
