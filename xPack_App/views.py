from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import RegistrarForm
from .models import Registrar
from django.contrib import messages




# Create your views here.

def admin_dashboard(request):
    from xPack_Registrar.models import Registry
    entry_list = Registry.objects.all()
    return render(request, 'dashboard/admin_dashboard.html', {'entry_list': entry_list})

def registry(request):
    from xPack_Registrar.models import Registry
    entry_list = Registry.objects.all()
    return render(request, 'dashboard/registry.html', {'entry_list': entry_list})

def devices(request):
    registrar_list = Registrar.objects.all()
    return render(request, 'dashboard/devices.html', {'registrar_list': registrar_list})

def stats(request):
    return render(request, 'dashboard/stats.html')

def dash_tech(request):
    return render(request, 'dashboard/dash_tech.html')

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
    return render(request, 'dashboard/add.html', {'form':form, 'submitted':submitted})


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
    return render(request, 'dashboard/update_registrar.html', {'registrar':registrar, 'form':form})
