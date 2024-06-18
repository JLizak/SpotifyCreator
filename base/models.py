from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)

class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    songs = models.ManyToManyField(Song)
    
   # class Meta:
   #     ordering = ["-updated", "-created"]
   # description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
   