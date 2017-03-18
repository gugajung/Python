from django.contrib import admin
from models import Aconteceu, ConteudoAconteceu

class AconteceuAdmin(admin.ModelAdmin):
    list_filter = ('titulo',)
    search_fields = ('titulo',)
    
class ConteudoAconteceuAdmin(admin.ModelAdmin):    
    search_fields = ('titulo','conteudo')
    
    class Media:
        js = (
              '/testes/django/matao4x4/media/js/nicEdit/nicEdit.js',
              '/testes/django/matao4x4/media/js/nicEdit/configCont.js',
              )
   
admin.site.register(Aconteceu, AconteceuAdmin)   
admin.site.register(ConteudoAconteceu, ConteudoAconteceuAdmin)     