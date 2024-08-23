from django import forms
from .models import *

class FormularioEstudante(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = ['nome', 'nota_final']