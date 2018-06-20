from django.db import models

# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200,default="")
    field = models.FileField(upload_to = 'media')