from django.shortcuts import render
from ..models import Registrar

def dashboard(request):
    """Registrar dashboard view"""
    return render(request, 'registrar/dashboard.html')

def devices(request):
    """Registrar devices view - shows devices assigned to this registrar"""
    # In a real implementation, you would filter by the current registrar
    registrar_devices = Registrar.objects.all()  # This should be filtered by current user
    return render(request, 'registrar/devices.html', {'devices': registrar_devices})

def profile(request):
    """Registrar profile management view"""
    return render(request, 'registrar/profile.html')

def reports(request):
    """Registrar reports view"""
    return render(request, 'registrar/reports.html')