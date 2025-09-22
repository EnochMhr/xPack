from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import RegistrarForm
from .models import Registrar
from django.contrib import messages
from .decorators import xpack_login_required

# Create your views here.

@xpack_login_required(admin_required=True)
def admin_dashboard(request):
    from xPack_Registrar.models import Registry, PackageAction
    from django.db.models import Count
    from django.utils import timezone
    from datetime import timedelta

    # Get members and visitors count
    members_count = Registry.objects.filter(membership='Member').count()
    visitors_count = Registry.objects.filter(membership='Visitor').count()

    # Get served and rejected packages count
    served_count = PackageAction.objects.filter(action='served').count()
    rejected_count = PackageAction.objects.filter(action='rejected').count()

    # Calculate 30-minute intervals for the last 3 hours
    now = timezone.now()
    intervals = []
    members_data = []
    visitors_data = []
    
    for i in range(6):  # 6 intervals of 30 minutes = 3 hours
        interval_end = now - timedelta(minutes=30 * i)
        interval_start = interval_end - timedelta(minutes=30)
        
        members = Registry.objects.filter(
            membership='Member',
            created_at__gte=interval_start,
            created_at__lt=interval_end
        ).count()
        
        visitors = Registry.objects.filter(
            membership='Visitor',
            created_at__gte=interval_start,
            created_at__lt=interval_end
        ).count()
        
        intervals.insert(0, interval_start.strftime('%H:%M'))
        members_data.insert(0, members)
        visitors_data.insert(0, visitors)
        
    # Calculate growth percentage for members (last 30 minutes)
    new_members = Registry.objects.filter(
        membership='Member',
        created_at__gte=now - timedelta(minutes=30)
    ).count()
    growth_percentage = round((new_members / members_count * 100), 1) if members_count > 0 else 0

    # Get all registry entries for the table
    entry_list = Registry.objects.all().order_by('-created_at')[:10]  # Show last 10 entries by default

    import json
    
    # Prepare chart data as a JSON string
    chart_data = {
        'intervals': intervals,
        'members': members_data,
        'visitors': visitors_data
    }
    
    context = {
        'members_count': members_count,
        'visitors_count': visitors_count,
        'served_count': served_count,
        'rejected_count': rejected_count,
        'growth_percentage': growth_percentage,
        'year': timezone.now().year,
        'entry_list': entry_list,
        'chart_data': json.dumps(chart_data)
    }
    
    return render(request, 'dashboard/admin_dashboard.html', context)

@xpack_login_required(admin_required=True)
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
