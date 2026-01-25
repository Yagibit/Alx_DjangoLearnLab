from django.db import models

class Book(models.Model):  # Ensure 'Book' is capitalized and spelled correctly
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()