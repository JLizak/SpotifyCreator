from django.forms import ModelForm
from .models import Playlist, Song

class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = '__all__'