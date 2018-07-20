from django.http import HttpResponse
from django.template import loader
from django.shortcuts import HttpResponse, get_object_or_404, render
from django.views import View, generic

from .models import Artist
# Create your views here.


class IndexView(View):
    template_name = 'history/index.html'

    def get(self, request):
        return HttpResponse('you are at the artist index')

class ArtistsView(generic.ListView):
    template_name = 'history/artists.html'
    context_object_name = 'artists'

    def get_queryset(self):
        return Artist.objects.all()

class DetailView(generic.DetailView):
    model = Artist
    template_name = 'history/detail.html'
