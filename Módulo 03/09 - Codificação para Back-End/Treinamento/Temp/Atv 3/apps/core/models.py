from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=254)
    imagem = models.ImageField(upload_to='cursos/', null=True, blank=True)

    def __str__(self):
        return self.titulo


class Aula(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    video_aula = models.FileField(upload_to='videos/', null=True, blank=True)
    material_complementar = models.FileField(upload_to='materiais/', null=True, blank=True)

    def __str__(self):
        return self.titulo


class Inscricao(models.Model):
    aluno = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_inscricao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Inscrição de {self.aluno} para {self.curso.titulo}'


class Certificado(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_emissao = models.DateTimeField(auto_now_add=True)
    arquivo_certificado = models.FileField(upload_to='certificados/')

    def __str__(self):
        return f'Certificado de {self.curso.titulo} | {self.aluno}'
