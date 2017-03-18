from django.contrib import admin
from matao4x4.acessorios.models import TipoAcessorio, MarcaAcessorio, Acessorio, \
    FotosAcessorio
from django import forms

class AcessorioForm(forms.ModelForm):
    valor = forms.DecimalField(max_digits=10, decimal_places=2, localize=True)
    class Meta:
        model = Acessorio

class AcessorioAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['nome', 'tipo', 'marca', 'valor',]
    list_filter = ['valor', 'marca',]
    
class FotosAcessorioAdmin(admin.ModelAdmin):
    list_display = ['acessorio']

#admin.site.register(TipoAcessorio)
#admin.site.register(MarcaAcessorio)
#admin.site.register(Acessorio, AcessorioAdmin)
#admin.site.register(FotosAcessorio, FotosAcessorioAdmin)