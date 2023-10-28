from django.db import models

class detalhecurso(models.Model):
    curso = models.CharField(max_length=100)
    turma = models.CharField(max_length=100)

# Create your models here.
