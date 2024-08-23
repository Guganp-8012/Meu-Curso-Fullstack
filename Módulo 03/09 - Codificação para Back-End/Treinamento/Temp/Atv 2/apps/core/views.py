from django.shortcuts import render, redirect
from .models import *
from .forms import *

def ViewIndex(request):
    busca = Produto.objects.all()
    return render(request, "index.html", {"produtos": busca})


def CriarCategoria(request):
    if request.method == "POST":
        nova_categoria = FormularioCategoria(request.POST)
        if nova_categoria.is_valid():
            nova_categoria.save()
            return redirect("pg_inicial")
    else:
        nova_categoria = FormularioCategoria()
    return render(request, "cadastro-categoria.html", {"formulario": nova_categoria})


def CriarProduto(request):
    if request.method == "POST":
        novo_produto = FormularioProduto(request.POST, request.FILES)
        if novo_produto.is_valid():
            novo_produto.save()
            return redirect("pg_inicial")
    else:
        novo_produto = FormularioProduto()
    return render(request, "cadastro-produto.html", {"formulario": novo_produto})


def EditarProduto(request, id_produto):
    busca = Produto.objects.get(id=id_produto)
    produto_editado = FormularioProduto(request.POST, instance=busca)    
    if produto_editado.is_valid():
        produto_editado.save()
        return redirect("pg_inicial")
    else:
        produto_editado = FormularioProduto()
    return render(request, "editar-produto.html", {"produtos": busca})

