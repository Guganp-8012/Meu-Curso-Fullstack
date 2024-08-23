from django.db import models

class Produto(models.Model):
    img_produto = models.ImageField(upload_to="media/fotos_produtos/")
    nome_produto = models.CharField(max_length=100)
    valor_com_desc = models.DecimalField(decimal_places=2, max_digits=6)
    valor_sem_desc = models.DecimalField(decimal_places=2, max_digits=6)
    descricao = models.CharField(max_length=254, max_digits=6)
    
    def __str__(self):
        return self.nome_produto
