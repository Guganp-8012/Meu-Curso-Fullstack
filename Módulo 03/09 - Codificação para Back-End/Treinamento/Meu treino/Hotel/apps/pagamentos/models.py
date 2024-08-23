from django.db import models

class DocPagamento(models.Model):
    faturas = models.CharField(max_length=254)
    recibos = models.CharField(max_length=254)

class FormaPagamento(models.Model):
    #pag_codigo =
    pag_descricao = models.CharField(max_length=254)