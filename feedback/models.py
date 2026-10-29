from django.db import models
from django.contrib.auth.models import User
from filim.models import Movie


class Review(models.Model):

    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    message = models.TextField()

    rating = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.movie.title