# coding: utf-8
'''
Created on 25/10/2011

@author: Matheus
'''
from django.contrib import admin
from sincomercio.arquivos.models import Arquivo, Categoria

class CategoriaAdmin(admin.ModelAdmin):
    pass 

class ArquivoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Arquivo, ArquivoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
