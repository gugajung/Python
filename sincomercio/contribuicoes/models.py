# -*- coding: utf-8 -*-
'''
Created on 06/09/2012

@author: Jonatas
'''
from django.db import models

escolhas = (
            ('A','Ativada'),
            ('D','Desativa')
        )

class Contribuicao(models.Model):
    class Meta:
        verbose_name = 'Nova Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ('-data',)
      
    titulo = models.CharField('Título', max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=escolhas)
    
    def __unicode__(self):
        return self.titulo
    
    def get_absolute_url(self):
        
        return "/lercontribuicao/%i/" % self.id

class ConteudoContribuicao(models.Model):
    class Meta:
        verbose_name = 'Conteudo Categoria'
        verbose_name_plural = 'Conteudo Categorias'
        
    titulo = models.CharField('Título', max_length=100)
    arquivo = models.FileField(upload_to = "arquivos" )
    categoria = models.ForeignKey(Contribuicao)
    def __unicode__(self):
        return self.titulo
