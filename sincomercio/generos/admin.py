# -*- coding: utf-8 -*-
from django.contrib import admin
from sincomercio.generos.models import Genero

class GeneroAdmin(admin.ModelAdmin):
    fieldsets = (
        ('',
           {'fields':('nome',)
        }),          
    )
    list_display = ('nome',)
    list_filter = ('nome',)
    search_fields = ('nome',)

admin.site.register(Genero, GeneroAdmin)