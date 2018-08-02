from django.urls import path

from . import views

app_name = 'history'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('artists/', views.ArtistsView.as_view(), name='artists'),
    # ex: /polls/5/results/
    path('artists/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('artists/add/', views.Artist_Form_View.as_view(), name='artist_form')
]