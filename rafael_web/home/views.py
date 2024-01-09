from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    return render(request, 'home/base.html')

def home(request):
    return render(request, 'home/base.html')

def services(request):
    return render(request, 'home/base.html')

def team(request):
    return render(request, 'home/base.html')

def contact(request):
    return render(request, 'home/base.html')

def blog(request):
    return render(request, 'home/base.html')
