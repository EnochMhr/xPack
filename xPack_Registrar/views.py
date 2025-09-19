from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistryForm, FamilyForm
from django.contrib import messages
from .models import Family,Registry

# Create your views here.

# def base(request):
#     return render(request, 'registrar/base.html')

def reg_dashboard(request):
    entry_list = Registry.objects.all()
    return render(request, 'registrar/reg_dashboard.html', {'entry_list': entry_list})

def family(request):
    fam_member_list = Family.objects.all()
    return render(request, 'registrar/family.html', {'fam_member_list': fam_member_list})

def packages(request):
    return render(request, 'registrar/packages.html')

def served(request):
    return render(request, 'registrar/served.html')

def reg_tech(request):
    return render(request, 'registrar/reg_tech.html')

def new_entry(request):
    submitted = False
    registry_form = RegistryForm()
    if request.method == "POST":
        form = RegistryForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/xPack_Registrar/new_entry/?submitted=True')
    
    else:
        form = RegistryForm
        if 'submitted' in request.GET:
            submitted = True
            messages.success(request, 'Registered successfully!') 
    return render(request, 'registrar/new_entry.html', {'registry_form':registry_form, 'submitted':submitted})
    # return render(request, 'registrar/new_entry.html', {'registry_form': registry_form})

def family_entry(request):
    submitted = False
    family_form = FamilyForm()
    if request.method == "POST":
        form = FamilyForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/xPack_Registrar/family_entry/?submitted=True')
    
    else:
        form = FamilyForm
        if 'submitted' in request.GET:
            submitted = True
            messages.success(request, 'Registered successfully!') 
    return render(request, 'registrar/family_entry.html', {'family_form':family_form, 'submitted':submitted})
    # return render(request, 'registrar/family_entry.html', {'family_form': family_form})