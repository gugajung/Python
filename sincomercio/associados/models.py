# -*- coding: utf-8 -*-
'''
Created on 29/10/2010

@author: Matheus
'''

from django.db import models

class Associado(models.Model):
    
    codigo_associado = models.CharField('Código do Associado', max_length=32)
    senha_associado = models.CharField('Senha do Associado', max_length=8, help_text='Máximo de 8 caracteres alfanuméricos')
    
    
    def __unicode__(self):
        return 'associado com o código: %s' % self.codigo_associado