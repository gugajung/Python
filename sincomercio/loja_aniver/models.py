# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import signals
from sincomercio.loja_aniver.signals import loja_post_save, loja_pre_delete

class LojaAniver(models.Model):
    class Meta:
        verbose_name = 'Lojas Aniversariantes'
        verbose_name_plural = verbose_name
        
    nome = models.CharField('Razão Social', max_length=100)
    descricao = models.CharField('Nome Fantasia', max_length=100)
    data_aniver = models.DateField('Data de Aniversário')
    foto_loja = models.ImageField('Foto da Loja', upload_to='imgs/lojas/',blank = True,null = True)
    foto_loja_menor = models.ImageField(blank=True,upload_to='imgs/lojas/')

    def __unicode__(self):
        return self.nome

signals.post_save.connect(loja_post_save, sender=LojaAniver)
signals.pre_delete.connect(loja_pre_delete,sender=LojaAniver)