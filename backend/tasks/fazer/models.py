from django.db import models


class Fazer(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=200)

