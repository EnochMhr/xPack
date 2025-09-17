from django.db import models


# Create your models here.

class Registrar(models.Model):
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

  
class Registry(models.Model):
    pass

class Family(models.Model):
    pass

class Packages(models.Model):
    pass

class Packages_served(models.Model):
    pass

class Packages_rejected(models.Model):
    pass


