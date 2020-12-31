from django.shortcuts import render
from .models import MainWhoWeAre, OurStory
from .serializers import MainWhoWeAreSerializer, OurStorySerializer
from rest_framework import viewsets 

# Create your views here.

class MainWhoweAreViewSet(viewsets.ModelViewSet):
    queryset = MainWhoWeAre.objects.all()
    serializer_class = MainWhoWeAreSerializer

class OurStoryViewSet(viewsets.ModelViewSet):
    queryset = OurStory.objects.all()
    serializer_class = OurStorySerializer