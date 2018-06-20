from django.db import models

# Create your models here.

class Note(models.Model):
    date_id = models.DateField()
    content = models.CharField(max_length=500)
   # text_inside = models.BooleanField(default=False)

    def __str__(self):
        return self.content