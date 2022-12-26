from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
