# -*- coding: utf-8 -*-
import os
import shutil
from PIL import Image
from django import forms
from django.conf import settings
from django.contrib import admin
from sincomercio.noticias.models import Noticia
from sincomercio.noticias.models import NoticiasTv
from sincomercio.imagens.models import ImagemNoticia
        
class CampoImagemNoticia(admin.StackedInline):
    model = ImagemNoticia
    extra = 1
    
    exclude = ('foto_media','slug')

class AdminNoticia(admin.ModelAdmin):
    fieldsets = (
       ('Sobre a Notícia', {
        'fields':('titulo','chamada','conteudo','fonte','fonte_url','status','audio','video')
        }),       
    )
    list_filter = ('titulo','data',)
    search_fields = ('titulo','fonte',)
    list_display = ('titulo', 'chamada', 'fonte', 'data', 'status')
    inlines = [CampoImagemNoticia]
    
    
    # formset - Campo Imagem da Notícia
    def save_formset(self, request, form, formset, change):
        campos = formset.save(commit = False)
        for campo in campos :
            ### INICIO TRATAMENTO DA IMAGEM ###
            nomeImg = campo.foto.name.split('/')[-1]
            
            enderecoParcial ='imgs/noticias/%d/min_%s'%(campo.noticia.id, nomeImg)
            endereco = os.path.join(settings.MEDIA_ROOT,enderecoParcial)
            
            original = os.path.join(settings.MEDIA_ROOT,'imgs/noticias/%s'%(nomeImg))
            novaImgPath = os.path.join(settings.MEDIA_ROOT, 'imgs/noticias/%d/med_%s' % (campo.noticia.id, nomeImg))
            
            campo.foto_media = enderecoParcial
            campo.save()
            
            tamanhos = (238,156)
            # ABRINDO IMAGEM ORIGINAL PARA LEITURA
            miniatura = Image.open(original, 'r')
            novaImg = miniatura.resize(tamanhos, Image.ANTIALIAS)
            novaImg.save(endereco)
            
            # MOVENDO A IMAGEM ORIGINAL PARA A PASTA DA NOTICIA
            campo.foto = 'imgs/noticias/%d/med_%s' % (campo.noticia.id, nomeImg)
            campo.save()
            
            # NOVO CAMINHO PARA IMAGEM DE TAMANHO MEDIO
            
            foto_resz = Image.open(original, 'r')
            novaFoto = foto_resz.resize((640,480), Image.ANTIALIAS)
            novaFoto.save(novaImgPath)
            
            os.remove(original)
            
class AdminNoticiaTv(admin.ModelAdmin):
    fieldsets = (
       ('Sobre a Notícia', {
        'fields':('titulo','link','status')
        }),       
    )
        
    list_filter = ('titulo','data',)
    list_display = ('titulo', 'data', 'status')

admin.site.register(Noticia, AdminNoticia)