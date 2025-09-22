from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import Registrar, AdminCredentials
from django.contrib.auth.hashers import check_password

class XPackAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        if not username or not password:
            return None

        # Let Django's default backend handle admin authentication
        if request and request.path.startswith('/admin/'):
            return None
            
        try:
            # First try registrar credentials
            try:
                registrar = Registrar.objects.get(name=username)  # Using name field from Registrar model
                if registrar.password == password:  # Using password field from Registrar model
                    # Create or get user for this registrar
                    user, created = User.objects.get_or_create(
                        username=username,
                        defaults={
                            'is_staff': False,
                            'is_superuser': False
                        }
                    )
                    if not created:  # Update existing user to ensure correct permissions
                        user.is_staff = False
                        user.is_superuser = False
                        user.save()
                    return user
            except Registrar.DoesNotExist:
                pass

            # Then try admin credentials (xPack_App admin, not Django admin)
            try:
                user = User.objects.get(username=username)
                if user.is_superuser:  # Skip if user is superuser - they should use Django admin login
                    return None
                admin_creds = AdminCredentials.objects.get(user=user)
                if admin_creds.password == password and admin_creds.is_active:
                    return user
            except (User.DoesNotExist, AdminCredentials.DoesNotExist):
                pass

        except Exception as e:
            print(f"Authentication error: {str(e)}")
        
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None