'''
Created on 11/09/2012

@author: Paulo
'''
from sincomercio.parceiros.models import Parceiro
from django.contrib import admin

class AdminParceiro (admin.ModelAdmin):
    list_filter = ('url','nomeRepresentante',)
    search_fields = ['nomeRepresentante']
    list_display = ('nomeRepresentante', 'image_img', 'url')

admin.site.register(Parceiro, AdminParceiro)