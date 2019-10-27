from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'home/index.html')

def projects_view(request):
    return render(request, 'projects/projects_view.html')

def web_view(request):
    return render(request, 'web/web_view.html')

def iot_view(request):
    return render(request, 'iot/iot_view.html')