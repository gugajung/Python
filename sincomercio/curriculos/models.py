# -*- coding: utf-8 -*-
'''
Created on 01/11/2010

@author: Matheus
'''

from django.db import models

class Curriculo(models.Model):
    
    opcoes_sex = (
        ('F','Feminino'),
        ('M','Masculino')          
    )
    
    opcoes_ensino = (
        ('C','Completo'),
        ('I','Incompleto')
    )
    
    opcoes_ensino_sup = (
        ('CO','Completo'),
        ('CR','Cursando'),
        ('T','Trancado'),
    )
    
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=14)
    endereco = models.CharField(max_length=100)
    data_nasc = models.DateField()
    idade = models.IntegerField(max_length=2)
    sexo = models.CharField(max_length=1, options=opcoes_sex)
    ensino_medio = models.CharField(max_length=1, options=opcoes_ensino)