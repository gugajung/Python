'''
Created on 06/12/2012

@author: User
'''

# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.fields.files import ImageField
from unicodedata import normalize


escolhas = (
        ('A','Ativada'),
        ('D','Desativada')
    )

class Banner (models.Model):
    
    descricao = models.CharField(max_length=50)
    imagem = ImageField(upload_to="img/banner")
    link = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, choices=escolhas)
    
    def __unicode__(self):
        
        return self.descricao    
    
    def save(self):
        nome = normalize('NFD', str(self.imagem).decode('utf-8')).encode('ASCII', 'ignore')
        self.imagem.name = nome
        super(Banner,self).save()
