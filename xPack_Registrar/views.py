from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import RegistryForm, FamilyForm
from .models import Family, Registry, PackageAction
from xPack_App.decorators import xpack_login_required
from xPack_App.models import Registrar, AdminCredentials  # Move imports to top

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

@xpack_login_required()
def served(request):
    served_packages = PackageAction.objects.filter(action='served').select_related('registry')
    return render(request, 'registrar/served.html', {'served_packages': served_packages})

@xpack_login_required()
def rejected(request):
    rejected_packages = PackageAction.objects.filter(action='rejected').select_related('registry')
    return render(request, 'registrar/rejected.html', {'rejected_packages': rejected_packages})

@xpack_login_required()
def account_view(request):
    try:
        # Check if user is an admin trying to access registrar views
        if AdminCredentials.objects.filter(user=request.user, is_active=True).exists():
            messages.error(request, 'Administrators cannot access registrar pages.')
            return redirect('admin_dashboard')
            
        # Get the registrar information for the logged-in user
        registrar = Registrar.objects.get(name=request.user.username)
        
        # Handle profile picture upload
        if request.method == 'POST' and request.FILES.get('profile_pic'):
            registrar.profile_pic = request.FILES['profile_pic']
            registrar.save()
            messages.success(request, 'Profile picture updated successfully!')
            return redirect('reg_account')
        
        # Ensure the registrar is accessing their own account
        if registrar.name != request.user.username:
            messages.error(request, 'You can only view your own account information.')
            return redirect('reg_dashboard')
        
        context = {
            'registrar': registrar,
            'user': request.user
        }
        return render(request, 'registrar/reg_account.html', context)
    except Registrar.DoesNotExist:
        messages.error(request, 'Registrar profile not found.')
        return redirect('reg_dashboard')
    except Exception as e:
        messages.error(request, 'An error occurred while loading your profile.')
        return redirect('reg_dashboard')

@xpack_login_required()
def mark_package_action(request, registry_id, action):
    try:
        registry = Registry.objects.get(id=registry_id)
        PackageAction.objects.create(registry=registry, action=action)
        messages.success(request, f'Package {action} successfully!')
    except Registry.DoesNotExist:
        messages.error(request, 'Registry entry not found.')
    
    return HttpResponseRedirect('/xPack_Registrar/packages/')

@xpack_login_required()
def reg_tech(request):
    return render(request, 'registrar/reg_tech.html')

@xpack_login_required()
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

@xpack_login_required()
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
    