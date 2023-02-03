from movieapp.models import Movie
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    
    # image of type ImageField and doesnt have text data so it needs to added explicity
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Movie
        fields = ('name', 'description', 'rating', 'image')

