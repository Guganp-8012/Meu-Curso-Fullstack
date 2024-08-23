from django.db import models

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_categoria
    

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    nome_produto = models.CharField(max_length=100)
    foto_produto = models.ImageField(upload_to="fotos/")
    descricao = models.CharField(max_length=100, default="descrição genérica [...]")
    valor = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.nome_produto