from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    nota_final = models.IntegerField()
    foto = models.ImageField(upload_to="fotos/")

    def __str__(self):
        return self.nome
    