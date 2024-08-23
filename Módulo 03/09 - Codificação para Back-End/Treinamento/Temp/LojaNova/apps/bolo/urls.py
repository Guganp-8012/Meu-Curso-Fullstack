from django.urls import path
from .views import *

urlpatterns = [
    path("", ViewIndex, name="pagina_index"),
    path("cadastro", CriarTarefa, name="pagina_cadastro")
]