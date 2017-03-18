# -*- coding: utf-8 -*-
from django.contrib import admin
from sincomercio.campanhas.models import Campanha
from sincomercio.imagens.models import ImagemCampanha

class CampoImagemCampanha(admin.StackedInline):
    model = ImagemCampanha
    extra = 0   
    exclude = ('fotoCampMenor',)
    
class AdminCampanha(admin.ModelAdmin):
    fieldsets = (
        ('Sobre a Campanha', {
            'fields': ('titulo','descricao', 'status')
        }),
    )

    list_display = ('titulo','descricao','data')
    inlines = [CampoImagemCampanha]
    list_filter = ('titulo',)
    search_fields = ('titulo','descricao',)

admin.site.register(Campanha, AdminCampanha)