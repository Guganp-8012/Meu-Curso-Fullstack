from django.db import models

class DocReserva(models.Model):
    class Meta:
        ordering = ('pk',)
        verbose_name = 'Reserva | Documento'
        verbose_name_plural = 'Reservas | Documentos'

    comprovante_reserva = models.CharField(max_length=254)
    termos_condicoes = models.TextField()


class Quarto(models.Model):
    qua_numero = models.PositiveIntegerField()
    qua_andar = models.PositiveIntegerField()


class Refeicao(models.Model):
    class Meta:
        verbose_name = 'Refeição'
        verbose_name_plural = 'Refeições'

    TIPO_REFEICAO = (
        ("C", "Café da Manhã"),
        ("A", "Almoço"),
        ("J", "Janta"),
        ("S", "Serviço de Quarto"),
        ("T", "Tudo Incluso")
    )

    tipo_ref = models.CharField(max_length=5, choices=TIPO_REFEICAO, null=True, blank=True)
    desc_ref = models.CharField(max_length=254)
    valor_ref = models.DecimalField(max_digits=5, decimal_places=2)


class Servico(models.Model):
    descricao = models.TextField()
    #valor_servico = models.FloatField()
    tipo_servico = models.CharField(max_length=254)
    #cod_servico
    #n_ocupantes = models.PositiveIntegerField()
    #res_entrada = models.DateTimeField()
    #res_saida = models.DateTimeField()
    #pag_codigo = models.ForeignKey()
    #inclui_ref = models.BooleanField()
    #refeicao = models.ForeignKey(Refeicao, on_delete=models.CASCADE)

class DetalhesAdicionais(models.Model):
    preferencias = models.CharField(max_length=254)
    condicao_especial = models.CharField(max_length=254, default="adicione aqui informações caso a pessoa necessita de algum tratamento mais delicado ou possui alguma deficiência.")