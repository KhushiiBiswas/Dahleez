from django.db import models
from focusarea.models import FocusArea

# Create your models here.
class Campaign(models.Model):
    Focusarea = models.OneToOneField(FocusArea, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, help_text="Campaign Name")
    description = models.TextField(max_length=1000, help_text='Description')
    image = models.ImageField(upload_to='campaign/')
    Focusarea = models.OneToOneField(FocusArea, on_delete=models.CASCADE) 


    
class Campaign_image(models.Model):
    Campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE)
    

class Campaign_figure(models.Model):
    Campaign = models.OneToOneField(Campaign, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)    
    figure = models.IntegerField()
