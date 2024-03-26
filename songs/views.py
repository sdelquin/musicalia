from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Song


def song_list(request: HttpRequest) -> HttpResponse:
    songs = Song.objects.all()
    return render(request, 'songs/song/list.html', dict(songs=songs))


def song_detail(request: HttpRequest, pk: int) -> HttpResponse:
    song = Song.objects.get(pk=pk)
    return render(request, 'songs/song/detail.html', dict(song=song))
