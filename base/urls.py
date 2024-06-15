'''URL patterns for base'''

from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.index, name='index'),
    path('playlists/', views.playlists, name='playlists'),
    path('playlists/create-playlist/', views.createPlaylist, name="create-playlist"),

    path('playlist/<str:pk>/', views.playlist, name='playlist'),
    path('playlists/<str:pk>/edit/', views.editPlaylist, name="edit"),
    path('playlists/<str:pk>/delete', views.deletePlaylist, name="delete"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
]