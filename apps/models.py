from unicodedata import category

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=222)


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=222)
    price = models.IntegerField()
    category = models.ForeignKey('apps.Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
