from django import forms
from .models import *

class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome_categoria']


class FormularioProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'