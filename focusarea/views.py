# from django.http import JsonResponse
# from django.shortcuts import render

# from .models import *
# # Create your views here.

# def allfocusarea(request):
#     focusareas = FocusArea.objects.all().order_by('-id')
#     return render(request,'focusarea.html',{'focusareas':focusareas})


# def focusarea_detail(request):
#     focusarea = FocusArea.objects.get(id=int(request.GET.get('id')))
#     response = {
#         'title': focusarea.title,
#         'description' : focusarea.description
#     }
#     return JsonResponse(response)
