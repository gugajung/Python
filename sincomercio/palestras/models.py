# -*- coding: utf-8 -*-

from django.db import models
from sorl.thumbnail.fields import ImageField

class Plestras(models.Model):
    class Meta:
        verbose_name = 'Palestra'
        verbose_name_plural = 'Palestras'
      
    titulo = models.CharField('Título', max_length=100)
    data = models.DateField()
    imagem = ImageField(upload_to= 'imgs/', blank = True, null = True)
    texto = models.TextField('Texto',blank = True, null = True)
    
    def __unicode__(self):
        
        return self.titulo