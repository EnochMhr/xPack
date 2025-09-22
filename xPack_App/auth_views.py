from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from xPack_App.models import Registrar, AdminCredentials

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Check if the user is a registrar
            try:
                registrar = Registrar.objects.get(name=username)
                messages.success(request, f'Welcome, {username}!')
                return redirect('reg_dashboard')
            except Registrar.DoesNotExist:
                pass
            
            # If not a registrar, check if admin
            try:
                admin_creds = AdminCredentials.objects.get(user=user)
                if admin_creds.is_active:
                    messages.success(request, f'Welcome, Admin {username}!')
                    return redirect('admin_dashboard')
            except AdminCredentials.DoesNotExist:
                pass
            
            # If we get here, user is authenticated but not a registrar or admin
            messages.error(request, 'Invalid account type')
            logout(request)  # Log them out since they shouldn't be logged in
            
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.html')

def custom_logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out!')
    return redirect('login')