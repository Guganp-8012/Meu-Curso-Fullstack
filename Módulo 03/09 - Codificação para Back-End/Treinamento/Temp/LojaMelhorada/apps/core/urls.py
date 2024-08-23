from django.urls import path
from .views import *

urlpatterns = [
    path("", ListaGeral, name="pg_inicial"),
    path("new-abencoado", CriarAbencoado, name="pg_new-abencoado"),
]
