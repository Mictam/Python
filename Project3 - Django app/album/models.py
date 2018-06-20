from django.db import models

# Create your models here.

class Photography(models.Model):
    photo_name = models.CharField(max_length=200)

    def __str__(self):
        return self.content