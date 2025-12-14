from django.db import models
from salas.models import Sala

class Aluno(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    data_nascimento = models.DateField()
    endereco = models.TextField()
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    data_inclusao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome