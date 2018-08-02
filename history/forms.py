from django.forms import ModelForm
from history import models

class Artist_Form(ModelForm):
    class Meta:
        model = models.Artist
        fields = ['artist_name']