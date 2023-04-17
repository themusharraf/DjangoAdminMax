from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=222)

    class Meta:
        verbose_name_plural = 'Kategoryalar'


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=222)
    price = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='media/products/')
    description = RichTextField(blank=True, null=True)
    category = models.ForeignKey('apps.Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Mahsulotlar'

    def __str__(self):
        return self.name
