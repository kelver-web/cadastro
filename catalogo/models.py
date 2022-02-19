from django.db import models
from django.utils import timezone

# Create your models here.


class Categoria(models.Model):
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.categoria


class Produto(models.Model):
    nome_produto = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    descricao = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_produto