from django.db import models


# Create your models here.

class Registrar(models.Model):
    name = models.CharField(max_length=20, null=True)
    contact = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=20, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)

