# -*- coding: utf-8 -*-
'''
Created on 29/10/2010

@author: Matheus
'''

from django.contrib import admin
from sincomercio.associados.models import Associado

class AssociadoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Associado, AssociadoAdmin)
