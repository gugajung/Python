from django.contrib import admin
from django.contrib.admin.options import TabularInline, StackedInline
from matao4x4.eventos.models import GaleriaEvento, ImagemGaleria, Eventos
from sorl.thumbnail.admin.compat import AdminImageMixin

class GaleriaEventos(TabularInline, StackedInline):
        model = GaleriaEvento
        extra = 0
    
class ImagemGalerias(AdminImageMixin, StackedInline):
    model = ImagemGaleria
    fields = ('imagem', 'capa')
    extra = 0
    
class AdminEventos(admin.ModelAdmin):
    list_filter = ('titulo',)
    search_fields = ('titulo',)
    list_display = ('titulo',)
    
#    def save_model(self, request, obj, form, change):
#        if obj.capa == 1:
#                capa = ImagemGaleria.objects.filter(galeriaEvento=obj.galeriaEvento, capa=1)
#                if not obj == capa:
#                    imagens = ImagemGaleria.objects.filter(galeriaEvento=obj.galeriaEvento)
#                    for imagem in imagens:
#                        if (capa == imagem):
#                            imagem.capa = 0
#                            imagem.save()   
#                admin.ModelAdmin.save_model(self, request, obj, form, change)

class AdminImagemGaleria(admin.ModelAdmin):
    list_display = ('galeriaEvento', 'imagem')
  

class AdminGaleriaEventos(admin.ModelAdmin):
    list_display = ('evento',)
    inlines = [ImagemGalerias]

admin.site.register(Eventos, AdminEventos)
admin.site.register(GaleriaEvento, AdminGaleriaEventos)
