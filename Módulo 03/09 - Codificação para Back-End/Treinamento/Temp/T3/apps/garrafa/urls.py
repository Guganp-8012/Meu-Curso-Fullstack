from django.urls import path
from .views import *

urlpatterns = [
    path("", ViewIndex, name="pagina_index"),
    path("login", ViewLogin, name="pagina_login"),
    path("ver_produto/<int:id_produto>/", DetalhesProduto, name="detalhes-produto")
]
