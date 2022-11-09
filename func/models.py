from django.db import models
from django.utils import timezone


class Profissao(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class ContractType(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    profissao = models.ForeignKey(Profissao, on_delete=models.DO_NOTHING)
    contract_type = models.ForeignKey(ContractType, on_delete=models.DO_NOTHING, default=1)
    salario = models.DecimalField(max_digits=7, decimal_places=2, default=1000.00)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')

    def __str__(self):
        return self.nome

