from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    

class SubCategoria(models.Model):
    nome = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome.nome
    

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(default="(aguardando descrição)")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    sub_categoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE, null=True, blank=True)
    estoque = models.IntegerField()
    preco = models.FloatField()

    def __str__(self):
        return self.nome
