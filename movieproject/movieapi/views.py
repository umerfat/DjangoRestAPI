from django.shortcuts import render
from rest_framework import generics
from movieapp.models import Movie
from .serializer import MovieSerializer

# Create your views here.

# This Django view list existing models (Movies in this case) and allows to create new models as well 
class MovieAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# This allows to retrieve, update and destry  movies indivitually 
class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

