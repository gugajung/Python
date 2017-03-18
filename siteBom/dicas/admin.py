# -*- coding: utf-8 -*-
'''
Created on 05/08/2010

@author: Matheus
'''

from django.contrib import admin
from siteBom.dicas.models import Dica

class AdminDica(admin.ModelAdmin):
    fieldsets =[
        (None, {'fields':['titulo', 'texto']}),
        
    ]

admin.site.register(Dica, AdminDica)