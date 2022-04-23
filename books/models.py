from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models

from django.db.models import Model, CASCADE


class Book(Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=CASCADE)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title
