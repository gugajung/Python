'''
Created on 06/12/2012

@author: User
'''

#coding:utf-8
from django.db import models
from django.db.models.fields.files import ImageField


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
