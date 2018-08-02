from django.http import HttpResponse
from django.template import loader
from django.shortcuts import HttpResponse, get_object_or_404, render, redirect
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

class DetailView(generic.DetailView):
    model = Artist
    template_name = 'history/detail.html'

class Artist_Form_View(FormView):
    template_name = 'history/artist_form.html'
    form_class = forms.Artist_Form

    def post(self, request):
        """method to post things to the artist collection

        Arguments:
            request {http request} -- auto passed in from the form. defines the http request

        Returns:
            http requests -- http requests based on form validation
        """
        # checks to see if the request method was a post
        if request.method == "POST":
            # if true it grabs the form post
            form = forms.Artist_Form(request.POST)
            # checks for form validation
            if form.is_valid():
                # saves the info the sql database
                post = form.save(commit=False)
                post.save()
                # returns the user to the artists list
                return HttpResponseRedirect('/history/artists')
        else:
            # else the user will be redirected back to the form
            form = forms.Artist_Form()

        return render(request, 'history/artist_form.html', {'form': form})