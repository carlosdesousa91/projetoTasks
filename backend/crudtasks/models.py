from django.db import models
from django.forms import ModelForm, Textarea

class Tasks(models.Model):
    #tId = models.CharField(max_length=20)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=15)

class Meta:
    db_table = "tasks"