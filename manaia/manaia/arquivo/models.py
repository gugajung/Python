'''
Created on 06/02/2013

@author: Paulo
'''
from django.db import models
from manaia.links.models import Categoria
from manaia.cliente.models import Cliente

class Categoria(models.Model):
    nome = models.CharField(max_length = 55)
    
    def __unicode__(self):
        
        return self.nome
class Arquivos(models.Model):
    nome = models.CharField(max_length = 55)
    data = models.DateField()
    arquivo = models.FileField(upload_to="arquivos")
    categoria = models.ForeignKey(Categoria)
    cliente = models.ForeignKey(Cliente)
    
    
    def __unicode__(self):        
        return self.nome