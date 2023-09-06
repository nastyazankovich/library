from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    gener = models.CharField(max_length=100)
    publication_date = models.DateTimeField()
    description = models.TextField()


class Library(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
# Create your models here.
