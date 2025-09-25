from django import forms
from django.forms import ModelForm
from .models import Registrar

class RegistrarForm(forms.ModelForm):
    class Meta:
        model = Registrar
        fields = ('__all__')
        labels = {
            'name': '',
            'contact': '',
            'location': '',
            'password': '',
            'profile_pic': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control focus-ring focus-ring-light', 'placeholder': 'Full Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control focus-ring focus-ring-light', 'placeholder': 'Contact'}),
            'location': forms.TextInput(attrs={'class': 'form-control focus-ring focus-ring-light', 'placeholder': 'Location'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control focus-ring focus-ring-light', 'placeholder': 'Password', 'id': 'user_pwd_reg', 'readonly': 'readonly' }),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }