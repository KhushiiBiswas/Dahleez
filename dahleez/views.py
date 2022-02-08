#from django.template import render
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import os


def homeView(request):
    if request.method == 'GET':
        imgarr = []
        for i in os.listdir(settings.MEDIA_ROOT + "/slides" ):
            imgarr.append(r"/media/slides/" + i)
        return render(request, 'index.html',{"arr":imgarr})

def aboutUs(request):
    if request.method == 'GET':      
        return render(request, 'about_us.html')

def focusArea(request):
    if request.method == 'GET':      
        return render(request, 'focus-areas.html')

def contact(request):
    if request.method == 'GET':      
        return render(request, 'contact.html')

def donate(request):
    if request.method == 'GET':      
        return render(request, 'donate.html')

def campaign(request):
    if request.method == 'GET':      
        return render(request, 'campaign.html')