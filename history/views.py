from django.http import HttpResponse
from django.template import loader
from django.shortcuts import HttpResponse, get_object_or_404, render
from django.views import View, generic
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from history import forms

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

    # def post(self, request, *args, **kwargs):
    #     print("this post is in artist view")
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/history/artists')

    #     return render(request, self.template_name, {'form': form})

class DetailView(generic.DetailView):
    model = Artist
    template_name = 'history/detail.html'

class Artist_Form_View(FormView):
    template_name = 'history/artist_form.html'
    form_class = forms.Artist_Form

    # def post(self, request, *args, **kwargs):
    #     form = forms.Artist_Form()
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/history/artists/')

    #     return render(request, self.template_name, {'form': form})

    def post(self, request, obj, form, change):
        obj.save()