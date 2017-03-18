# -*- coding: utf-8 -*-
from django.db import models

class Genero(models.Model):
    class Meta:
        verbose_name = 'Novo Gênero'
        verbose_name_plural = 'Gêneros dos Filmes'
        
    nome = models.CharField('Gênero', max_length=100)
    num_filmes = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return self.nome
    
    def natural_key(self):
        return (self.nome,)