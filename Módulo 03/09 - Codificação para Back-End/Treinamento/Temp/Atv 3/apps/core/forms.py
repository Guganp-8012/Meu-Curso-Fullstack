from .models import *
from django import forms

class FormularioCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class FormularioAula(forms.ModelForm):
    class Meta:
        model = Aula
        fields = '__all__'

class FormularioInscricao(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = '__all__'


class FormularioCertificado(forms.ModelForm):
    class Meta:
        model = Certificado
        fields = '__all__'