from django.contrib import admin
from matao4x4.anuncios.forms import AnunciantesAdminForm
from matao4x4.anuncios.models import Anunciante, Evento


class AnuncianteAdmin(admin.ModelAdmin):
    form = AnunciantesAdminForm
    search_fields = ['anunciante']
    list_display = ['anunciante', 'link']
    
class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo','data','cidade','estado',]
    list_filter = ['data','cidade','estado',]
    search_fields = ['titulo',]
    prepopulated_fields = {"slug" : ("titulo",)}

admin.site.register(Anunciante, AnuncianteAdmin)
admin.site.register(Evento, EventoAdmin)
