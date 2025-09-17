from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import RegistrarForm
from .models import Registrar
from django.contrib import messages




# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def registry(request):
    return render(request, 'registry.html')

def devices(request):
    registrar_list = Registrar.objects.all()
    return render(request, 'devices.html', {'registrar_list': registrar_list})

def stats(request):
    return render(request, 'stats.html')

def tech(request):
    return render(request, 'tech.html')

def add(request):
    submitted = False
    if request.method == "POST":
        form = RegistrarForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/xPack_App/add/?submitted=True')
    
    else:
        form = RegistrarForm
        if 'submitted' in request.GET:
            submitted = True
            messages.success(request, 'Registrar added successfully!') 
    return render(request, 'add.html', {'form':form, 'submitted':submitted})


def delete_registrar(request, id):
    registrar = Registrar.objects.get(pk=id)
    registrar.delete()
    return redirect('devices')
  
def update_registrar(request, id):
    registrar = Registrar.objects.get(pk=id)
    form = RegistrarForm(request.POST or None, instance=registrar)

    if form.is_valid():
        form.save()
        return redirect('devices')
    return render(request, 'update_registrar.html', {'registrar':registrar, 'form':form})
