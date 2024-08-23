from django.db import models

class Comunicacao(models.Model):
    #cliente = models.OneToOneField()
    telefone_celular = models.PositiveIntegerField()
    #email = models.ForeignKey()
    confirmacao_de_reserva = models.BooleanField()
    receber_notificacoes = models.BooleanField()
