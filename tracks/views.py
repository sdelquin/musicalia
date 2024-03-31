from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Track


def track_list(request: HttpRequest) -> HttpResponse:
    tracks = Track.objects.all()
    return render(request, 'tracks/track/list.html', dict(tracks=tracks))


def track_detail(request: HttpRequest, pk: int) -> HttpResponse:
    track = Track.objects.get(pk=pk)
    return render(request, 'tracks/track/detail.html', dict(track=track))
