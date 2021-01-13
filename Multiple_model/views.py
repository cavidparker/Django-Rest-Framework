from django.shortcuts import render
from .models import Play,Poem
from .serializers import PoemSerializer, PlaySerializer

from drf_multiple_model.views import ObjectMultipleModelAPIView

# Create your views here.

class TextAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': Play.objects.all(), 'serializer_class': PlaySerializer},
        {'queryset': Poem.objects.all(), 'serializer_class': PoemSerializer},
        # {'queryset': Poem.objects.filter(style='Sonnet'), 'serializer_class': PoemSerializer},

    ]
