# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.contrib import admin
from sincomercio.imagens.models import ImagemNoticia, ImagemCampanha

class FormImagemNoticia(forms.ModelForm):
    class Meta:
        model = ImagemNoticia

class AdminImagemNoticia(admin.ModelAdmin):
    list_display = ('noticia','titulo',)
    list_filter = ('noticia',)
    search_fields = ('noticia',)
    
 
#admin.site.register(ImagemVideo)
##admin.site.register(ImagemNoticia, AdminImagemNoticia)
#admin.site.register(ImagemCampanha)