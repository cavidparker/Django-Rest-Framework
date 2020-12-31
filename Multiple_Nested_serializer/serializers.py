from .models import MainWhoWeAre, OurStory
from rest_framework import serializers


class OurStorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OurStory
        fields = ['id','title', 'description']


class MainWhoWeAreSerializer(serializers.ModelSerializer):
    story = OurStorySerializer(many = True, read_only = True) 
    class Meta:
        model = MainWhoWeAre
        fields = ['id','page_title_english', 'page_template_english','page_heading_english','story']        

 
