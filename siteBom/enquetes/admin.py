# -*- coding: utf-8 -*-
'''
Created on 05/08/2010

@author: Matheus
'''

from django.contrib import admin
from siteBom.enquetes.models import Enquete, Escolha


class EscolhaInline(admin.TabularInline):
    model = Escolha
    extra = 3
    
class EnqueteAdmin(admin.ModelAdmin):
    fieldsets =[
        (None, {'fields':['titulo']}),
        
    ]
    
    inlines = [EscolhaInline]
    search_fields = ['titulo']
    
admin.site.register(Enquete, EnqueteAdmin)
