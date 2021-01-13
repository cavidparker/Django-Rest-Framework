from rest_framework import serializers
from .models import Play, Poem, Slider

class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ('id','genre','title','pages')

class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = ('id','title','style','stanzas','lines')

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('id', 'image', 'image_sd')
