from django.db import models


# Create your models here.

class Registrar(models.Model):
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

  
