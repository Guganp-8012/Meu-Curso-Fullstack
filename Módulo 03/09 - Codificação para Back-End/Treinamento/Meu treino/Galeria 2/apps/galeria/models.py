from django.db import models
from apps.core.models import Usuario
    

class Foto(models.Model):
    nome = models.CharField(max_length=50, default="Imagem ")
    foto = models.CharField(max_length=100, default="models.ImageField(upload_to='photos/')")
    ultima_modificacao = models.DateTimeField()
    usuario = models.ManyToManyField(Usuario)

    def __str__(self):
        return self.nome


class Album(models.Model):
    titulo = models.CharField(max_length=100)
    privado = models.BooleanField(default=False)    
    data_de_criacao = models.DateTimeField()
    fotos = models.ManyToManyField(Foto)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + " | " + self.usuario.nome