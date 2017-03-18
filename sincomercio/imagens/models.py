# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import signals
from sincomercio.acoes_sociais.models import AcaoSocial
from sincomercio.campanhas.models import Campanha
from sincomercio.imagens.signals import imagem_acao_post_save, \
    imagem_campanha_post_save
from sincomercio.loja_aniver.models import LojaAniver
from sincomercio.noticias.models import Noticia
from sincomercio.utils.signals_comuns import slug_pre_save
from sincomercio.videoteca.models import Videoteca

class ImagemNoticia(models.Model):
    class Meta:
        verbose_name = 'Imagem da notícia'
        verbose_name_plural = verbose_name
    
    titulo = models.CharField('Descrição', blank=True, max_length=100)
    slug = models.SlugField('Legenda',
        null=True,
        blank=True,
        max_length=100,
        help_text='Deixar em branco. O próprio sistema irá criar a legenda.',
    )
    noticia = models.ForeignKey(Noticia)
    foto = models.ImageField(
        'Imagem',
        null=True,
        blank=True,
        upload_to='imgs/noticias/',
        help_text='Selecione a imagem de tamanho original',)
    foto_media = models.ImageField(
        'Imagem (Tamanho médio)',
        null=True,
        blank=True,
        upload_to='imgs/noticias/',
        help_text='Deixar em branco. O próprio sistema irá gerar uma imagem em tamanho médio',)
        
    def __unicode__(self):
        return 'Imagem'
    
class ImagemCampanha(models.Model):
    class Meta:
        verbose_name = 'Imagem da Campanha'
        verbose_name_plural = 'Imagens da Campanha'
        
    campanha = models.ForeignKey(Campanha)
    fotoCamp = models.ImageField(
            'Banner',
            null=True,
            blank=True,
            upload_to='imgs/campanhas/',
            help_text='Tamanho Original')
    fotoCampMenor = models.ImageField(null=True, blank=True, upload_to='imgs/campanhas/menores/')
    
    def __unicode__(self):
        return 'Imagem da Campanha'
    
class ImagemAcoesSociais(models.Model):
    class Meta:
        verbose_name = 'Foto - Ação Social'
        verbose_name_plural = 'Fotos - Ação Social'
    
    acao = models.ForeignKey(AcaoSocial)    
    foto_acao = models.ImageField('Foto',
            null=True,
            blank=True,
            upload_to='imgs/acoes_sociais/')
    foto_acao_menor = models.ImageField(null=True, blank=True, upload_to='imgs/acoes_sociais/menores/')
    
    def __unicode__(self):
        return 'Imagem'
    
  
  

    

    
signals.pre_save.connect(slug_pre_save, sender=ImagemNoticia)
signals.post_save.connect(imagem_acao_post_save, sender=ImagemAcoesSociais)
signals.post_save.connect(imagem_campanha_post_save, sender=ImagemCampanha)