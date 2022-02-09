from django.db import models

# Create your models here.
class FocusArea(models.Model):
    title = models.CharField(max_length=40, help_text="Focus Area's title", default = "")
    description = models.TextField(help_text='Description')
    focusArea_img = models.ImageField(upload_to='focus_area/')

class Focusarea_figure(models.Model):
    focusArea = models.OneToOneField(FocusArea, on_delete=models.CASCADE)
    title = models.CharField(max_length=40) 
    Figure = models.IntegerField()  