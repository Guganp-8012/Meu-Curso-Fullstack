from django.db import models
#from ..turmas.models import Materia

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="fotos_perfil/", null=True, blank=True)
    #turma = 
    #extracurricular =

    def __str__(self):
        return self.nome


class DadosPessoais(models.Model):
    TIPO_SEXO = (
        ("M", "Masculino"),
        ("F", "Feminino")
    )
    
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    sexo = models.CharField(max_length=2, choices=TIPO_SEXO)
    nascimento = models.DateField()
    cpf = models.PositiveIntegerField()
    rg = models.PositiveIntegerField()
    historico_escolar = models.FileField(upload_to="doc_aluno/")
    #boletim =
    #n_faltas =  #frequencia

    def __str__(self):
        return "Dados Pessoais | " + self.aluno.nome
    

class Frequencia(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    faltas = models.PositiveIntegerField(default=0)
    justificadas = models.PositiveIntegerField(default=0)
    presenca = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Frequência | " + self.aluno.nome