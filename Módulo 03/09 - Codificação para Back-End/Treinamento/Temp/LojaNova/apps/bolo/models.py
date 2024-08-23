from django.db import models

class Tarefa(models.Model):
    ESTADO_CHOICES = [
        ("PENDENTE", "Pendente"),
        ("EM_PROGRESSO", "Em Progresso"),
        ("CONCLUIDA", "Concluída"),
    ]

    nome_tarefa = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_conclusão = models.DateField()
    estado = models.CharField(max_length=3, choices=ESTADO_CHOICES)
    responsavel = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_tarefa
    