# -*- coding: utf-8 -*-
from django.contrib import admin
from sincomercio.eventos.models import Eventos, GaleriaEvento, ImagemGaleria
from django.contrib.admin.options import StackedInline, TabularInline
from sorl.thumbnail.admin.compat import AdminImageMixin

class GaleriaEventos(TabularInline, StackedInline):
        model = GaleriaEvento
        extra = 0
    
class ImagemGalerias(AdminImageMixin, StackedInline):
    model = ImagemGaleria
    fields = (('imagem'),)
    extra = 0
    
class AdminEventos(admin.ModelAdmin):
    list_filter = ('titulo','data',)
    search_fields = ('titulo','data')
    list_display = ('titulo', 'data', 'Chamada')
    
#    inlines = [GaleriaEventos]

class AdminImagemGaleria(admin.ModelAdmin):
    list_display = ('galeriaEvento','imagem')

class AdminGaleriaEventos(admin.ModelAdmin):
    list_display = ('evento',)
    
    inlines = [ImagemGalerias]

admin.site.register(Eventos, AdminEventos)
admin.site.register(GaleriaEvento, AdminGaleriaEventos)
#admin.site.register(ImagemGaleria, AdminImagemGaleria)
 
#admin.site.register(ImagemVideo)
##admin.site.register(ImagemNoticia, AdminImagemNoticia)
#admin.site.register(ImagemCampanha)