from django.db import models
from django.contrib.auth.models import User

from filim.models import Movie


class Song(models.Model):

    moviename = models.ForeignKey(Movie,on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    track_number = models.PositiveIntegerField()

    singer = models.CharField(max_length=150)

    duration = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        last_song_object = Song.objects.filter(moviename=self.moviename).last()

        if last_song_object:

            self.track_number = last_song_object.track_number + 1

        else:

            self.track_number= 1

        return super().save(*args, **kwargs)

