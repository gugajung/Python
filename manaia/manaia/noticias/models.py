# -*- coding: utf-8 -*-
'''
Created on 06/12/2012

@author: User
'''

from django.db import models


escolhas = (
        ('A','Ativada'),
        ('D','Desativada')
    )

class Noticia(models.Model):
    class Meta:
        verbose_name = 'Nova Notícia'
        verbose_name_plural = 'Notícias'
        ordering = ('-data',)
      
    titulo = models.CharField('Título', max_length=100)
    conteudo = models.TextField('Conteúdo')
    fonte_url = models.URLField('URL da Fonte', max_length=100, null=True, blank=True, help_text='Exemplo: http://www.nomedosite.com.br/')
    data = models.DateField()
    status = models.CharField(max_length=1, choices=escolhas)
    
    def __unicode__(self):
        return self.titulo
    
    @models.permalink
    def get_absolute_url(self):
        return ('manaia.views.VerNoticias', [str(self.id)])

    
