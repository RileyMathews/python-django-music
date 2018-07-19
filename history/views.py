from django.http import HttpResponse
from django.template import loader
from django.shortcuts import HttpResponse, get_object_or_404, render

from .models import Artist
# Create your views here.

def index(request):
    return HttpResponse("you are at the artist index")

def artists(request):
    artists = Artist.objects.all()
    template = loader.get_template('history/artists.html')
    context = {
        'artists': artists,
    }
    return HttpResponse(template.render(context, request))

def detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    template = loader.get_template('history/detail.html')
    context = {
        'artist': artist,
    }
    return HttpResponse(template.render(context, request))