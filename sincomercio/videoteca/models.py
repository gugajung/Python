# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import signals
from sincomercio import settings
from sincomercio.generos.models import Genero
from sincomercio.utils.signals_comuns import slug_pre_save
from sincomercio.videoteca.signals import video_post_save, video_pre_delete
from unicodedata import normalize
import md5
import os


class Genero(models.Model):
    class Meta:
        verbose_name = 'Novo Gênero'
        verbose_name_plural = 'Gêneros dos Filmes'
        
    nome = models.CharField('Gênero', max_length=100)
    num_filmes = models.IntegerField(blank=True)
    
    def __unicode__(self):
        return self.nome
    
    def natural_key(self):
        return (self.nome,)

class Videoteca(models.Model):
    class Meta:
        verbose_name = 'Novo Filme'
        verbose_name_plural = 'Filmes'
        ordering = ('-data',)
        
    escolhas = (
     ('A','Ativado'),
     ('D','Desativado'),            
    )
    
    titulo = models.CharField('Título', max_length=100)
    codigo = models.CharField('Código do Filme', max_length=32)
    slug = models.SlugField(max_length=100)
    ano = models.IntegerField('Ano',max_length=4, blank=True,null=True)
    genero = models.ForeignKey(Genero)
    status = models.CharField(max_length=1, choices=escolhas, default='A')
    capa = models.ImageField(upload_to='imgs/videos/')
    capa_menor = models.ImageField(upload_to='imgs/videos/')
    data = models.DateField(auto_now_add=True)
    
    def __unicode__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('sincomercio.videoteca.views.video', kwargs={'slug':self.slug})

# METODO PARA ADICIONAR AUTOMATICAMENTE UM SLUG        
signals.pre_save.connect(slug_pre_save, sender=Videoteca)

signals.post_save.connect(video_post_save, sender=Videoteca)
signals.pre_delete.connect(video_pre_delete, sender=Videoteca)