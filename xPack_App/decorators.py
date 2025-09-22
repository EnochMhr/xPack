from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps
from .models import AdminCredentials, Registrar

def xpack_login_required(view_func=None, admin_required=False):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Check if user is authenticated
            if not request.user.is_authenticated:
                messages.error(request, 'Please log in to access this page.')
                return redirect('login')  # Assuming 'login' is your login URL name

            # For admin-only views
            if admin_required:
                try:
                    # Check if user has admin credentials
                    admin_creds = AdminCredentials.objects.get(user=request.user, is_active=True)
                except AdminCredentials.DoesNotExist:
                    messages.error(request, 'You must be an admin to access this page.')
                    return redirect('login')

            # For registrar views, check if user is a registrar
            else:
                try:
                    # Try to get registrar credentials
                    registrar = Registrar.objects.get(name=request.user.username)
                except Registrar.DoesNotExist:
                    # If not a registrar and not requesting admin page, redirect
                    if not admin_required:
                        messages.error(request, 'You must be a registrar to access this page.')
                        return redirect('login')

            return view_func(request, *args, **kwargs)
        return _wrapped_view

    if view_func:
        return decorator(view_func)
    return decorator