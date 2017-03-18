# -*- coding: utf-8 -*-
'''
Created on 06/12/2012

@author: User
'''
from django.contrib import admin
from manaia.noticias.models import Noticia

class NoticiasAdmin(admin.ModelAdmin):
    class Media:
        js = (
              '/site/media/js/nicEdit/nicEdit.js',
              '/site/media/js/nicEdit/configCont.js',
              )
    

admin.site.register(Noticia, NoticiasAdmin)