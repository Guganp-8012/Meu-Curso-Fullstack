from django.shortcuts import render
from .models import *

def ViewIndex(request):
    produtos_lista = Produto.objects.all()
    return render(request, "index.html", {"produtos": produtos_lista})

def ViewLogin(request):
    return render(request, "login.html")

def DetalhesProduto(request, id_produto):
    busca = Produto.objects.get(id=id_produto)
    return render(request, "detalhes-produto.html", {"produto": busca})