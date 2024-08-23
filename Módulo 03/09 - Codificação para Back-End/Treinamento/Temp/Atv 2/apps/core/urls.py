from django.urls import path
from .views import *

urlpatterns = [
    path("", ViewIndex, name="pg_inicial"),
    path("cadastro-produto/", CriarProduto, name="form_produto"),
    path("cadastro-categoria/", CriarCategoria, name="form_categoria"),
    path("detalhes-produto/<int:id_produto>/", EditarProduto, name="pg_detalhes")
]
