'''
Created on 06/02/2013

@author: Paulo
'''

from django.contrib import admin
from manaia.arquivo.models import Categoria

class CategoriaAdmin(admin.ModelAdmin):
    
    model = Categoria
        
    search_fields = ('nome',)

admin.site.register(Categoria, CategoriaAdmin)
