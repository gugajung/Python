# -*- coding: utf-8 -*-
'''
Created on 05/12/2012

@author: User
'''

from django.db import models

class Categoria(models.Model):
    """
        Representa uma categoria
    """
    
    nome = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.nome

class Link(models.Model):
    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links Úteis'
    
    nomecategoria = models.ForeignKey(Categoria, verbose_name = 'Nome Categoria',related_name= "nomeCategorias")
    site_nome = models.CharField('Título do Site', max_length=100, blank=False)
    site_url = models.URLField('URL do Site', max_length=100, help_text='Exemplo: http://www.nomedosite.com.br/')
    
    def __unicode__(self):
        return self.site_nome