from django import forms
from django.forms import ModelForm
from .models import Registry, Family

class RegistryForm(forms.ModelForm):
    class Meta:
        model = Registry
        fields = ('__all__')
        labels = {
            'name': '',
            'contact': '',
            'membership':'',
            'family':'',
            'gender': '',
            'location': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control focus-ring focus-ring-light', 'placeholder': 'Full Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control focus-ring focus-ring-light', 'placeholder': 'Contact'}),
            'location': forms.TextInput(attrs={'class': 'form-control focus-ring focus-ring-light', 'placeholder': 'location'}),
         }

class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['name', 'contact', 'family_rep']
        labels = {
            'name': '',
            'contact': '',
            'family_rep': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control focus-ring focus-ring-light', 'placeholder': 'Family Member Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control focus-ring focus-ring-light', 'placeholder': 'Contact'}),
            'family_rep': forms.TextInput(attrs={'class': 'form-control focus-ring focus-ring-light', 'placeholder': 'Family Representative Name'}),
        }
