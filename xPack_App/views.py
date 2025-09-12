from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sayHello(request):
    return render(request, 'base.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def registry(request):
        return render(request, 'registry.html')


def devices(request):
    return render(request, 'devices.html')


def stats(request):
    return render(request, 'stats.html')


def tech(request):
    return render(request, 'tech.html')


