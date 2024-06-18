from django.shortcuts import render, redirect
from .models import Song, Playlist, User
from .forms import PlaylistForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from urllib.parse import urlencode
from ..SpotifyCreator import settings

@login_required
def spotify_login(request):
    params = {
        'response_type': 'code',
        'client_id': settings.SPOTIFY_CLIENT_ID,
        'redirect_url': settings.SPOTIFY_REDIRECT_URL
    }
    auth_url = f'https://accounts.spotify.com/authorize?{urlencode(params)}'
    return redirect(auth_url)


def loginPage(request):
    page = 'login'

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Incorrect username")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("base:index")
        else:
            messages.error(request, "Incorrect username or password")
    context = {'page': page}
    return render(request, "base/login_register.html", context)


def logoutUser(request):
    logout(request)
    return redirect("base:index")


def registerUser(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("base:index")
        else:
            messages.error(request, "Error occured during registration")

    return render(request, 'base/login_register.html', {"form": form})


def index(request):
    return render(request, 'base/index.html')


@login_required(login_url='/login')
def playlists(request):
    playlists = Playlist.objects.all()
    context = {"playlists": playlists}
    return render(request, 'base/playlists.html', context)


def playlist(request, pk):
    playlist = Playlist.objects.get(id=pk)
    context = {"playlist": playlist}
    return render(request, 'base/playlist.html', context)


def createPlaylist(request):
    form =  PlaylistForm()
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("base:playlists")
    context = {"form": form}
    return render(request, 'base/playlist_form.html', context)


def editPlaylist(request, pk):
    playlist = Playlist.objects.get(id=pk)

    form = PlaylistForm(instance=playlist)
    if request.method == "POST":
        form = PlaylistForm(request.POST, instance=playlist)
        if form.is_valid():
            form.save()
            return redirect("base:playlists")
        
    context = {"form": form}
    return render(request, 'base/playlist_form.html', context)


def deletePlaylist(request, pk):
    playlist = Playlist.objects.get(id=pk)
    if request.method == "POST":
        playlist.delete()
        return redirect("base:playlists")
    
    return render(request, "base/delete.html", {"obj": playlist})