'''
Created on 05/12/2012

@author: User
'''
from django.contrib import admin
from manaia.links.models import Link, Categoria

class CategoriaAdmin(admin.ModelAdmin):
#    list_filter = ('nome',)
#    search_fields = ('nome',)
    pass

class AdminLinks(admin.ModelAdmin):
    list_display = ('site_nome','site_url')

admin.site.register(Link, AdminLinks)
admin.site.register(Categoria, CategoriaAdmin)