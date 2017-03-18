# -*- coding: utf-8 -*-
'''
Created on 06/09/2012

@author: Jonatas
'''
from django.contrib import admin
from sincomercio.contribuicoes.models import Contribuicao, ConteudoContribuicao
from django.contrib.admin.options import StackedInline

class ConteudoAdminContribuicao(StackedInline):
    
    model = ConteudoContribuicao
    extra = 0

class AdminContribuicao(admin.ModelAdmin):
    
    class Media:
        js = (
              '/midias/js/nicEdit/nicEdit.js',
              '/midias/js/nicEdit/configCont.js',
              )
    list_filter = ('titulo','data',)
    search_fields = ('titulo',)
    list_display = ('titulo', 'data', 'status')
    inlines = [ConteudoAdminContribuicao]
    
admin.site.register(Contribuicao, AdminContribuicao)    
