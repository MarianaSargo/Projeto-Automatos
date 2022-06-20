from django.db import models

# Create your models here.

class Automato(models.Model):
    EstadoInicial = models.CharField(max_length=10000, default = 'A')
    EstadoFinal = models.CharField(max_length=10000, default = 'A')
    Transicoes = models.CharField(max_length=10000, default = 'A')
    Estados = models.CharField(max_length=10000, default = 'A')
    Alfabeto = models.CharField(max_length=10000, default = 'A')
    Descricao = models.CharField(max_length=10000, default = 'A')

    def __str__(self):
        return self.Descricao[:300]

class MTuring(models.Model):
    EstadoInicial = models.CharField(max_length=10000, default='A')
    EstadoFinal = models.CharField(max_length=10000, default='A')
    Transicoes = models.CharField(max_length=10000, default='A')
    Estados = models.CharField(max_length=10000, default='A')
    Alfabeto = models.CharField(max_length=10000, default='A')
    Descricao = models.CharField(max_length=10000, default='A')

    def __str__(self):
        return self.Descricao[:300]


