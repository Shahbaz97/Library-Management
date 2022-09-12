from unicodedata import name
from django.db import models
from django.urls import reverse

# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        return self.name

# book relation that has 2 foreign key author language


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    language = models.ForeignKey(
        'Language', on_delete=models.SET_NULL, null=True)
    available_copies = models.IntegerField()


# return canonical url for an object


    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    # __str__ method is used to override default string returnd by an object
    def __str__(self):
        return self.title
