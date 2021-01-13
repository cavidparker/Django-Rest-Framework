from .models import MainWhoWeAre, OurStory, OurService
from rest_framework import serializers



class MainWhoWeAreSerializer(serializers.ModelSerializer):
    # our_story = serializers.StringRelatedField(many = True, read_only = True)
    class Meta:
        model = MainWhoWeAre
        fields = ['id','page_heading_english','our_story']


class OurServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurService
        fields = ['ourservice_title','description','image', 'image_sd']


class OurStorySerializer(serializers.ModelSerializer):
    # StoryBy = serializers.StringRelatedField(many = True, read_only = True)
    StoryBy = MainWhoWeAreSerializer(many = True, read_only = True)
    # serviceBy = OurServiceSerializer(many =True, read_only = True)
    serviceBy = serializers.StringRelatedField(many = True, read_only = True)
    class Meta: 
        model = OurStory
        fields = ['id','title', 'description','StoryBy', 'serviceBy']


       

 
