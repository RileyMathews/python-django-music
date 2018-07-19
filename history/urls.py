from django.urls import path

from . import views

app_name = 'history'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('artists/', views.artists, name='artists'),
    # ex: /polls/5/results/
    path('artists/<int:artist_id>/', views.detail, name='detail'),
]