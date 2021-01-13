from django.shortcuts import render
from .models import MainWhoWeAre, OurStory,OurService
from .serializers import MainWhoWeAreSerializer, OurStorySerializer, OurServiceSerializer
from rest_framework import viewsets 

# Create your views here.

class MainWhoweAreViewSet(viewsets.ModelViewSet):
    queryset = MainWhoWeAre.objects.all()
    serializer_class = MainWhoWeAreSerializer

class OurStoryViewSet(viewsets.ModelViewSet):
    queryset = OurStory.objects.all()
    serializer_class = OurStorySerializer

class OurServiceViewSet(viewsets.ModelViewSet):
    queryset = OurService.objects.all()
    serializer_class = OurServiceSerializer