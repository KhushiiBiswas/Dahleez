from django.contrib import admin
from campaigns.models import Campaign, Campaign_figure, Campaign_image

# Register your models here.
admin.site.register(Campaign)
admin.site.register(Campaign_image)
admin.site.register(Campaign_figure)