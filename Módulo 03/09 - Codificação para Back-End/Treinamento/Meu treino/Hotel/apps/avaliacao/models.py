from django.db import models
from apps.core.models import Perfil

class Feedback(models.Model):
    ESCOLHA = (
        ("1", "Péssimo"),
        ("2", "Ruim"),
        ("3", "Mediano"),
        ("4", "Bom"),
        ("5", "Excelente")        
    )

    cliente = models.OneToOneField(Perfil, on_delete=models.CASCADE, null=True, blank=True)
    avalie = models.CharField(max_length=5, choices=ESCOLHA, null=True, blank=True)
    comentario = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return "Feedback de " + Perfil.cliente
    