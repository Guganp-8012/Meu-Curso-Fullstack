from django.db import models
from apps.core.models import Perfil

class DadosPessoais(models.Model):
    TIPO_SEXO = (
        ("M", "Masculino"),
        ("F", "Feminino")
    )
    
    #cliente = models.OneToOneField(Perfil, on_delete=models.CASCADE)
    #pri_nome = models.CharField(max_length=50) #já tem esse tipo de informação na tabela
    #ult_nome = models.CharField(max_length=50)
    #cpf = models.PositiveIntegerField()
    #rg = models.PositiveIntegerField()
    sexo = models.CharField(max_length=2, choices=TIPO_SEXO)
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    #passaporte = models.PositiveIntegerField(null=True, blank=True)
    #cnh = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return " | Documentos" # Perfil.cliente + 
    
