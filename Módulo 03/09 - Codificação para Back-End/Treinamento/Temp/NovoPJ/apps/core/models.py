from django.db import models

class Tarefa(models.Model):
    ESTADO_CHOICES = [
        ("PENDENTE", "Pendente"),
        ("EM_PROGRESSO", "Em Progresso"),
        ("CONCLUIDA", "Concluída"),
    ]

    nome_tarefa = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100, null=True, blank=True)
    data_inicio = models.DateField(default='00/00/0000...')
    data_conclusão = models.DateField(default='00/00/0000...')
    estado = models.CharField(max_length=12, choices=ESTADO_CHOICES)
    responsavel = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_tarefa
