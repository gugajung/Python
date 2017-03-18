'''
Created on 07/12/2012

@author: User
'''

from django.db import models

class Newsletters(models.Model):
    class Meta:
        verbose_name = 'Newsletters'
        verbose_name_plural = 'Newsletters'
    
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.nome