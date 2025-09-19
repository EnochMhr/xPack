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

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    name = models.CharField(max_length= 20, null=True)
    contact = models.CharField(max_length=20, null=True)
    membership = models.CharField(max_length=10, choices=mem_type, null=True)
    family = models.CharField(max_length=10, choices=has_family,  null=True)
    gender = models.CharField(max_length=10, null=True, choices=GENDER_CHOICES)
    location = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Family(models.Model):
     name = models.CharField(max_length= 20, null=True)
     contact = models.CharField(max_length=20, null=True)
     family_rep = models.CharField(max_length=20, null=True)
    #  created_at = models.DateTimeField(auto_now_add=True)

    # we may use this to reference the main table
        # family_rep = models.ForeignKey(Registry, on_delete=models.CASCADE) 
    # this should reference the family member registered

# class Reg_Login(models.Model):
#     username = models.CharField(max_length=10, null=True)
#     password = models.CharField(max_length=10, null=True)

class PackageAction(models.Model):
    ACTION_CHOICES = [
        ('served', 'Served'),
        ('rejected', 'Rejected'),
    ]
    
    registry = models.ForeignKey(Registry, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']


