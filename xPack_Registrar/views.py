from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistryForm, FamilyForm
from django.contrib import messages
from .models import Family, Registry, PackageAction
from xPack_App.decorators import xpack_login_required

# Create your views here.

# def base(request):
#     return render(request, 'registrar/base.html')

@xpack_login_required()
def reg_dashboard(request):
    entry_list = Registry.objects.all()
    return render(request, 'registrar/reg_dashboard.html', {'entry_list': entry_list})

@xpack_login_required()
def family(request):
    fam_member_list = Family.objects.all()
    return render(request, 'registrar/family.html', {'fam_member_list': fam_member_list})

@xpack_login_required()
def packages(request):
    registry_list = Registry.objects.all()
    return render(request, 'registrar/packages.html', {'registry_list': registry_list})

def served(request):
    served_packages = PackageAction.objects.filter(action='served').select_related('registry')
    return render(request, 'registrar/served.html', {'served_packages': served_packages})

def rejected(request):
    rejected_packages = PackageAction.objects.filter(action='rejected').select_related('registry')
    return render(request, 'registrar/rejected.html', {'rejected_packages': rejected_packages})

def mark_package_action(request, registry_id, action):
    try:
        registry = Registry.objects.get(id=registry_id)
        PackageAction.objects.create(registry=registry, action=action)
        messages.success(request, f'Package {action} successfully!')
    except Registry.DoesNotExist:
        messages.error(request, 'Registry entry not found.')
    
    return HttpResponseRedirect('/xPack_Registrar/packages/')

def reg_tech(request):
    return render(request, 'registrar/reg_tech.html')

def new_entry(request):
    submitted = False
    if request.method == "POST":
        registry_form = RegistryForm(request.POST)
        if registry_form.is_valid():
            registry_form.save()
            messages.success(request, 'Registered successfully!')
            return HttpResponseRedirect('/xPack_Registrar/new_entry/?submitted=True')
    else:
        registry_form = RegistryForm()
    
    if 'submitted' in request.GET:
        submitted = True
        
    return render(request, 'registrar/new_entry.html', {'registry_form': registry_form, 'submitted': submitted})

def family_entry(request):
    submitted = False
    if request.method == "POST":
        family_form = FamilyForm(request.POST)
        if family_form.is_valid():
            family_form.save()
            messages.success(request, 'Family member registered successfully!')
            return HttpResponseRedirect('/xPack_Registrar/family_entry/?submitted=True')
    else:
        family_form = FamilyForm()
        if 'submitted' in request.GET:
            submitted = True
            messages.success(request, 'Family member registered successfully!')
    
    # Get list of registered members for context
    registry_members = Registry.objects.all()
    
    return render(request, 'registrar/family_entry.html', {
        'family_form': family_form,
        'submitted': submitted,
        'registry_members': registry_members
    })
    