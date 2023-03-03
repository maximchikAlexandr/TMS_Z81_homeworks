from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pseudonym = models.CharField(max_length=250)
    country = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return self.pseudonym


class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)

    class Meta:
        ordering = ['title', 'author']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        return ", ".join(genre.name for genre in self.genre.all())


class BookInstance(models.Model):
    STATUSES = (("On Loan", "On Loan"),
                ("Available", "Available"),
                ("Reserved", "Reserved"),
                ("Lost", "Lost"))

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 blank=True, null=True)
    due_back = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUSES, default="Available")

    def __str__(self):
        return self.book.title

    def get_absolute_url(self):
        return reverse('book-instance-detail', args=[str(self.id)])
