from django.urls import path
from .views import *

urlpatterns = [
    path("", ViewCadastro, name="pagina_index"),
    path("cadastro", CriarCelular, name="pagina_cadastro")
]