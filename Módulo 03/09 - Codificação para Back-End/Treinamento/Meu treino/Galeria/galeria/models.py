from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    

class Album(models.Model):
    nome = models.CharField(max_length=100)
    privado = models.BooleanField(default=False) 
    data_de_criacao = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
    

class Foto(models.Model):
    nome = models.CharField(max_length=50, default="Imagem ")
    foto = models.CharField(max_length=50, default="Imagine uma foto")
    ultima_modificacao = models.DateTimeField(null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
