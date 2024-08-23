from django.urls import path
from .views import *

urlpatterns = [
    path("", VerIndex, name="pg_inicial")
]