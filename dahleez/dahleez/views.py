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