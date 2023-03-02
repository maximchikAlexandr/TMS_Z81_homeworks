from django.db import models


class Zodiac(models.Model):
    latin_name = models.CharField(max_length=15)
    russian_name = models.CharField(max_length=15)
