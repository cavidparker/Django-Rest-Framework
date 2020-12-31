from django.db import models

# Create your models here.
  
class OurStory(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()

    def __str__(self):
        return self.title

class MainWhoWeAre(models.Model):
    page_title_english = models.CharField(max_length = 200)    
    page_template_english = models.CharField(max_length = 200)
    page_heading_english = models.CharField(max_length = 200)
    our_story = models.ForeignKey(OurStory, on_delete=models.CASCADE, related_name='story',blank = True)
    def __str__(self):
        return self.page_title_english

