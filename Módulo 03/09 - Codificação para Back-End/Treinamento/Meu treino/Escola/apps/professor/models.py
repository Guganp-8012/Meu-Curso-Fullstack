from django.db import models
from ..turmas.models import Materia

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return self.nome
    