from django.db import models

# Create your models here.

class Registry(models.Model):
    mem_type = [
        ('Member', 'Member'),
        ('Visitor', 'Visitor'),
    ]

    has_family = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]

    name = models.CharField(max_length= 20, null=True)
    contact = models.CharField(max_length=20, null=True)
    membership = models.CharField(max_length=10, choices=mem_type, null=True)
    family = models.CharField(max_length=10, choices=has_family,  null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Family(models.Model):
     name = models.CharField(max_length= 20, null=True)
     contact = models.CharField(max_length=20, null=True)
     family_rep = models.CharField(max_length=20, null=True)
    #  created_at = models.DateTimeField(auto_now_add=True)


    # we may use this to reference the main table
        # family_rep = models.ForeignKey(Registry, on_delete=models.CASCADE) 
    # this should reference the family member registered

class Packages(models.Model):
    # in here we should have the registry but with another field of action whether serve or reject
    pass

class Packages_served(models.Model):
     # in here we should refence the name contact and membership type of the person served from the main table
    # created_at = models.DateTimeField(auto_now_add=True)
    pass

class Packages_rejected(models.Model):
     # in here we should refence the name contact and membership type of the person who rejects from the main table
    # created_at = models.DateTimeField(auto_now_add=True)
    pass


