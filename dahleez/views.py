#from django.template import render
from turtle import title
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import os

from focusarea.models import FocusArea, Focusarea_figure
from campaigns.models import Campaign

def homeView(request):
    if request.method == 'GET':
        focusArea = FocusArea.objects.all()
        campaign = Campaign.objects.all()
        # imgarr = []
        # for i in os.listdir(settings.MEDIA_ROOT + "/slides" ):
        #     imgarr.append(r"/media/slides/" + i)
        return render(request, 'index.html', {"focusareas": focusArea,"campaigns": campaign})

def aboutUs(request):
    if request.method == 'GET':      
        return render(request, 'about_us.html', )

def focusArea(request):
    if request.method == 'GET': 
        # fa = request.GET.get("fa")

        # print(fa)
        # focusarea = FocusArea.objects.get(title = "fa")
        focusarea = FocusArea.objects.all()
        focusarea_figure  = Focusarea_figure.objects.all()
        return render(request, 'focus-areas.html', {"focusareas": focusarea, "figures": focusarea_figure})

def contact(request):
    if request.method == 'GET':      
        return render(request, 'contact.html')

def donate(request):
    if request.method == 'GET':      
        return render(request, 'donate.html')

def campaign(request):
    if request.method == 'GET': 
        campaign = Campaign.objects.all()     
        return render(request, 'campaign.html', {"campaigns": campaign})
