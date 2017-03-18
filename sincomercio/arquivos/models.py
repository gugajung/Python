# coding: utf-8
from django.db import models

# Create your models here.

class Categoria(models.Model):
    """
        Representa uma categoria
    """
    
    nome = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.nome

class Arquivo(models.Model):
    """
        Representa um arquivo
    """
    
    arquivo = models.FileField(upload_to='arquivos/')
    categoria = models.ForeignKey(Categoria)
    descricao = models.TextField('Descrição')
    ano = models.IntegerField()
    
    def __unicode__(self):
        return '{0}'.format(self.arquivo.name)
       
