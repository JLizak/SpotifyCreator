from django.contrib import admin
from .models import Song, Playlist, User

admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(User)