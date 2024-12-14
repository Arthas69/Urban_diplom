from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    publication_date = models.DateField()
    # image = models.CharField(max_length=100, blank=True)
    # image = models.ImageField(upload_to='books', height_field=300, width_field=400)
    image = models.ImageField(upload_to='books/', null=True, blank=True)
    # rating = models.DecimalField(max_length=)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title


class Review(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"Review by {self.author}"


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, default="Genre")
    description = models.TextField(blank=True, null=True)
    books = models.ManyToManyField(Book, related_name='genres')

    def __str__(self):
        return self.name
