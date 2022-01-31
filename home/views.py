from django.shortcuts import render
from django.views.generic.base import TemplateView

def home(request):
    return render(request, "home/index.html")

def companyinfo(request):
    return render(request, "home/companyinfo.html")

def service(request):
    return render(request, "home/service.html")