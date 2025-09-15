from django.shortcuts import render,redirect
from django.http import HttpResponse
# from .forms import Registrar 
from .models import Registrar


# Create your views here.

def sayHello(request):
    return render(request, 'base.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def registry(request):
        return render(request, 'registry.html')

# for the manage devices template
def devices(request):
    
    return render(request, 'devices.html')


def stats(request):
    return render(request, 'stats.html')


def tech(request):
    return render(request, 'tech.html')

def add(request):
    return render(request, 'add.html')
