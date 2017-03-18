# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import signals
from sincomercio.campanhas.signals import campanha_post_save, \
    campanha_pre_delete
from sincomercio.utils.signals_comuns import slug_pre_save

class Campanha(models.Model):
    class Meta:
        verbose_name = 'Nova Campanha'
        verbose_name_plural = 'Campanhas'
        ordering = ('-data',)
    
    escolhas = (
        ('A','Ativada'),
        ('D','Desativada')
    )
    
    titulo = models.CharField('Título', max_length=100)
    slug = models.SlugField(max_length=100)
    descricao = models.TextField('Descrição')
    data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=escolhas)

    def __unicode__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('sincomercio.campanhas.views.campanha', kwargs={'slug': self.slug})
    
signals.pre_save.connect(slug_pre_save, sender=Campanha)
signals.post_save.connect(campanha_post_save, sender=Campanha)
signals.pre_delete.connect(campanha_pre_delete, sender=Campanha)