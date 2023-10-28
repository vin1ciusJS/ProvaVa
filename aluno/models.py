from django.db import models

class aluno(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)
    datanascimento = models.DateField(max_length=100)