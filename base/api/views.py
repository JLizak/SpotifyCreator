from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Playlist
from .serializers import PlaylistSerializer
from django.contrib.auth import authenticate
from rest_framework import status


@api_view(['GET'])
def getPlaylists(request):
    playlists = Playlist.objects.all()
    serializer = PlaylistSerializer(playlists, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getPlaylist(request, pk):
    playlist = Playlist.objects.get(id=pk)
    serializer = PlaylistSerializer(playlist, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def loginView(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        return Response({"message": "Login succesful"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)