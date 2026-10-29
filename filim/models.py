from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):

    LANGUAGE_CHOICES = [
        ('malayalam', 'Malayalam'),
        ('tamil', 'Tamil'),
        ('hindi', 'Hindi'),
        ('english', 'English'),
        ('telugu', 'Telugu'),
        ('others', 'Others'),
    ]

    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('thriller', 'Thriller'),
        ('horror', 'Horror'),
        ('drama', 'Drama'),
        ('others', 'Others'),
    ]

    title = models.CharField(max_length=200)

    run_time = models.PositiveIntegerField()

    rating = models.DecimalField(max_digits=3,decimal_places=1)

    language = models.CharField(max_length=20,choices=LANGUAGE_CHOICES)

    genre = models.CharField(max_length=20,choices=GENRE_CHOICES)

    released_year = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
