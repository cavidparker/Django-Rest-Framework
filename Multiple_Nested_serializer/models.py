from django.db import models

# Create your models here.

class OurService(models.Model):
    ourservice_title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to = "our_service_image")
    image_sd = models.ImageField(upload_to = "ourservice_sd")

    def __str__(self):
        return self.ourservice_title

  
class OurStory(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()

    def __str__(self):
        return self.title


class MainWhoWeAre(models.Model):
    page_heading_english = models.CharField(max_length = 200)
    our_story = models.ForeignKey(OurStory, on_delete=models.CASCADE, related_name ='StoryBy')
    our_service = models.ForeignKey(OurService, on_delete=models.CASCADE, related_name = 'serviceBy')

    def __str__(self):
        return self.page_heading_english 
        

