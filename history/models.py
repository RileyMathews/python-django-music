import datetime

from django.db import models
from django.utils import timezone


class Artist(models.Model):
    artist_name = models.CharField(max_length=200)

class Song(models.Model):
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=200)
    song_length = models.IntegerField(default=200)
