from django.shortcuts import render
from .models import *
from .forms import *

def ViewIndex(request):
    busca_celular = Tarefa.objects.all()
    return render(request, "index.html", {"tarefas": busca_celular})

def CriarTarefa(request):
    
    if request.method == "POST":
        nova_tarefa = FormularioTarefa(request.POST)
        nova_tarefa.save()
        nova_tarefa = FormularioTarefa()
    else:
        nova_tarefa = FormularioTarefa()
    return render(request, "cadastro.html", {"formulario": nova_tarefa})
