from django import forms
from django.forms import ModelForm
from .models import Registrar

class RegistrarForm(forms.ModelForm):
    class Meta:
        model = Registrar
        fields = ('__all__')