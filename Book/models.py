from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)


class Book(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    img = models.ImageField(upload_to='img')
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
