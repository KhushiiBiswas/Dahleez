from django.db import models

class Slide(models.Model):
    slide_img = models.ImageField(upload_to='slides/')

class StoriesThatInspire(models.Model):
    name = models.CharField(max_length= 40)
    designation = models.CharField(max_length= 40)  
    image = models.ImageField(upload_to='stories/')
    descrition = models.TextField(help_text= "Description")




