# -*- coding: utf-8 -*-
'''
Created on 29/06/2011

@author: Matheus
'''

from django.contrib import admin
from sincomercio.comunicados.models import Comunicado

class ComunicadoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comunicado, ComunicadoAdmin)