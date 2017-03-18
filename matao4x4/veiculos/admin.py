from django.contrib import admin
from matao4x4.veiculos.models import MarcaCarro, Veiculos, FotosVeiculo

class VeiculosAdmin(admin.ModelAdmin):
    search_fields = ['modelo']
    list_display = ['modelo', 'marca', 'valor',]
    list_filter = ['marca']
    
class FotosVeiculoAdmin(admin.ModelAdmin):
    list_display = ['veiculo']

admin.site.register(MarcaCarro)
admin.site.register(Veiculos, VeiculosAdmin)
admin.site.register(FotosVeiculo, FotosVeiculoAdmin)