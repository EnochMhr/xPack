from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.db import transaction
from xPack_App.models import AdminCredentials

class Command(BaseCommand):
    help = 'Creates a new xPack admin user with associated credentials'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username for the admin')
        parser.add_argument('password', type=str, help='Password for the admin')
        parser.add_argument(
            '--update',
            action='store_true',
            help='Update if user exists'
        )

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        update = options.get('update', False)

        try:
            # Use transaction to ensure both User and AdminCredentials are created or neither is
            with transaction.atomic():
                user = User.objects.filter(username=username).first()
                
                if user:
                    if not update:
                        raise CommandError(f'User {username} already exists. Use --update to update their credentials.')
                    
                    # Update existing user
                    user.set_password(password)
                    user.is_staff = False
                    user.save()
                    
                    # Update or create admin credentials
                    admin_cred, created = AdminCredentials.objects.update_or_create(
                        user=user,
                        defaults={
                            'password': password,
                            'is_active': True
                        }
                    )
                    
                    self.stdout.write(self.style.SUCCESS(f'Updated existing xPack admin user "{username}"'))

                # Create new user
                else:
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        is_staff=False,  # No access to Django admin site
                        is_superuser=False  # Not a superuser
                    )

                    # Create the AdminCredentials
                    admin_cred = AdminCredentials.objects.create(
                        user=user,
                        password=password,  # Using the same password for both Django and xPack auth
                        is_active=True
                    )

                    self.stdout.write(self.style.SUCCESS(
                        f'Successfully created new xPack admin user "{username}"'
                    ))
                self.stdout.write(f'Username: {username}')

        except Exception as e:
            raise CommandError(f'Failed to create admin user: {str(e)}')