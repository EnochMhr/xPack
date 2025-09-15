from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from ..forms import RegistrarForm
from ..models import Registrar




# Create your views here.

def sayHello(request):
    return render(request, 'base.html')

def dashboard(request):
    return render(request, 'admin/dashboard.html')

def registry(request):
    return render(request, 'admin/registry.html')

def devices(request):
    registrar_list = Registrar.objects.all()
    return render(request, 'admin/devices.html', {'registrar_list': registrar_list})

def stats(request):
    return render(request, 'admin/stats.html')

def tech(request):
    return render(request, 'admin/tech.html')

def add(request):
    submitted = False
    if request.method == "POST":
        form = RegistrarForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('?submitted=True')
    
    else:
        form = RegistrarForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'admin/add.html', {'form':form, 'submitted':submitted})

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
    return render(request, 'admin/update_registrar.html', {'registrar':registrar, 'form':form})
