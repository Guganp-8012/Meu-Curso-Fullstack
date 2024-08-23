from django.shortcuts import render, redirect
from .models import *
from .forms import *

def ViewCadastro(request):
    busca_celular = Celular.objects.all()
    return render(request, "index.html", {"celulares": busca_celular})

def CriarCelular(request):
    if request.method == "POST":
        novo_celular = FormularioCelular(request.POST)
        novo_celular.save()
        novo_celular = FormularioCelular()
    else:
        novo_celular = FormularioCelular()
    return render(request, "cadastro.html", {"formulario": novo_celular})
