from rest_framework import serializers
from .models import Play, Poem

class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ('id','genre','title','pages')

class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = ('id','title','style','stanzas','lines')
