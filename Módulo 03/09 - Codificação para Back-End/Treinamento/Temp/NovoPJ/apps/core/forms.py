from django import forms
from .models import *

class FormularioTarefa(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'