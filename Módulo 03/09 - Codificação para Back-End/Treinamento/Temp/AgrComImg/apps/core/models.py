from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    foto = models.ImageField(upload_to="fotos")

    def __str__(self):
        return self.nome
    