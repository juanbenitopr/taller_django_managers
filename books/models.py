from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models

from django.db.models import Model, CASCADE, Avg


class BookTopRatingManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-rating')

    def top_three(self):
        return super().get_queryset().order_by('-rating')[:3]

    def top_five(self):
        return super().get_queryset().order_by('-rating')[:5]


class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')

    def avg_rating(self):
        return self.get_queryset().aggregate(avg_rating=Avg('rating'))


class Book(Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=CASCADE)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookManager()
    top_rating = BookTopRatingManager()

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title
