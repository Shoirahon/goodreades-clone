from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField()
    isbn = models.CharField(max_length=17)


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    bio = models.TextField()


class BookAuthor(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)


class Review(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    stars_given = models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])
