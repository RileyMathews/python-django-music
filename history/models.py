import datetime

from django.db import models
from django.utils import timezone


class Artist(models.Model):
    artist_name = models.CharField(max_length=200)

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=200)
    song_length = models.IntegerField(default=200)

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=200)
    songs = models.ManyToManyField(Song, through='Album_Song')

class Album_Song(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
