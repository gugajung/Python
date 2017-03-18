# -*- coding: utf-8 -*-
from django.db import models
from sincomercio import settings
from django.db.models import signals
from sincomercio.comunicados.signals import deletaImagemComunicado

# Create your models here.

class Comunicado(models.Model):
    
    titulo = models.CharField('Título', max_length=255)
    texto = models.TextField('Comunicado', blank=True, null=True)
    imagem = models.ImageField('Banner', upload_to='comunicados/', blank=True, null=True)
    data = models.DateField(auto_now_add=True)
    periodo_de = models.DateField(blank=False, null=False)
    periodo_ate = models.DateField(blank=False, null=False)
    
    def __unicode__(self):
        return self.titulo
    
    @classmethod
    def getComunicados(self, data):
        return self.objects.filter(periodo_de__lte = data, periodo_ate__gte = data)

signals.pre_delete.connect(deletaImagemComunicado, Comunicado)
