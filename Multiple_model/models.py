from django.db import models

# Create your models here.

class Play(models.Model):
    genre = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    pages = models.IntegerField()

class Poem(models.Model):
    title = models.CharField(max_length=200)
    style = models.CharField(max_length=100)
    lines = models.IntegerField()
    stanzas = models.IntegerField()

class Slider(models.Model):
    image = models.ImageField(upload_to = "our_value_image")
    image_sd = models.ImageField(upload_to = "our_value_image_sd")