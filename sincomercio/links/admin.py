'''
Created on 27/10/2010

@author: Matheus
'''
# -*- coding: utf-8 -*-
from django.contrib import admin
from sincomercio.links.models import Link

class AdminLinks(admin.ModelAdmin):
    list_display = ('site_nome','site_url','site_descricao')

admin.site.register(Link, AdminLinks)
