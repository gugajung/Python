# -*- coding: utf-8 -*-
from PIL import Image
from django import forms
from django.conf import settings
from django.contrib import admin
from sincomercio.acoes_sociais.models import AcaoSocial
from sincomercio.imagens.models import ImagemAcoesSociais
import os

class CampoImagemAcoesSociais(admin.StackedInline):
    model = ImagemAcoesSociais
    extra = 1
    
    exclude = ('foto_acao_menor',)

class FormImagemSocial(forms.ModelForm):
    class Meta:
        model = ImagemAcoesSociais

class AdminAcoesSociais(admin.ModelAdmin):
    fieldsets = (
     ('Sobre a Ação Social',
      {'fields': ('titulo','descricao','status') 
     }),
    )
    list_display = ('titulo','data','status')
    inlines = [CampoImagemAcoesSociais]
    list_filter = ('titulo',)
    search_fields = ('titulo','descricao',)
