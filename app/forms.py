from django import forms
from django.forms import ModelForm
from django.forms import widgets, DateInput
from .models import *


class UsuarioForm(forms.ModelForm):   

    class Meta:
        model = Usuario
        fields = ['nome', 'data_nascimento', 'login', 'senha']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome do usuário ...'}),
            'data_nascimento': DateInput(attrs={'type': "date"}),
            'login': forms.TextInput(attrs={'placeholder': 'Digite um login ...'}),
            'senha': forms.PasswordInput(),          
    }