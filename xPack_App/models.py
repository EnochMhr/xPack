from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AdminCredentials(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Admin: {self.user.username}"

class Registrar(models.Model):
    name = models.CharField(max_length=20, null=True)
    contact = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
