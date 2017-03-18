# -*- coding: utf-8 -*-
'''
Created on 27/10/2010

@author: Matheus
'''

from django.db import models

class Link(models.Model):
    class Meta:
        verbose_name_plural = 'Links Úteis'
    
    site_nome = models.CharField('Título do Site', max_length=100, blank=False)
    site_url = models.URLField('URL do Site', max_length=100, help_text='Exemplo: http://www.nomedosite.com.br/')
    site_descricao = models.CharField('Descrição', max_length=100, help_text='Uma breve descrição sobre o site.')
    
    def __unicode__(self):
        return self.site_nome