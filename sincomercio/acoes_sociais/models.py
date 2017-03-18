# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import signals
from sincomercio.utils.signals_comuns import slug_pre_save 
from sincomercio.acoes_sociais.signals import acao_post_save, acao_pre_delete

class AcaoSocial(models.Model):
    class Meta:
        verbose_name = 'Nova Ação'
        verbose_name_plural = 'Ações Sociais'
        ordering = ('-data',)
    
    escolhas = (
        ('A','Ativada'),
        ('D','Desativada')
    )
    
    titulo = models.CharField('Título', max_length=100)
    slug = models.SlugField(max_length=100)
    descricao = models.TextField('Descrição')
    data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices = escolhas)

    def __unicode__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('sincomercio.acoes_sociais.views.acao', kwargs={'slug':self.slug})
    
    
#class Imagem(models.Model): 
#    
#    descricao =models.CharField(max_length=100)
#    foto = models.ImageField(upload_to = 'midia/fotos')
#    
#    def __unicode__(self):
#        return self.descricao   

signals.pre_save.connect(slug_pre_save, sender=AcaoSocial)
signals.post_save.connect(acao_post_save, sender=AcaoSocial)
signals.pre_delete.connect(acao_pre_delete, sender=AcaoSocial)