from django.db import models

class Slides(models.Model):
    slide_img = models.ImageField(upload_to='slides/')