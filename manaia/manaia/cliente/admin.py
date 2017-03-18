'''
Created on 20/07/2012

@author: Administrador
'''

from django.contrib import admin
from manaia.cliente.models import Cliente
from django.contrib.admin.options import StackedInline
from manaia.arquivo.models import Arquivos
from django.contrib.auth.admin import UserAdmin
from manaia.cliente.forms import FormClienteAlterar, FormClienteAdicionar,\
    FormCadastrar
from django.utils.translation import ugettext_lazy as _


class ArquivoLine(StackedInline):
    
    model = Arquivos
    extra = 0
     

class ClienteAdmin(UserAdmin):
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email','endereco','telefone')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ),
    )
    ValorInline = False
    model = Cliente
    form = FormClienteAlterar
    add_form = FormCadastrar    
    
    def get_form(self, request, obj=None, **kwargs):
        if obj is not None:
            self.inlines = [ArquivoLine]
        else:
            self.inlines = []
        return UserAdmin.get_form(self, request, obj=obj, **kwargs)
    

admin.site.register(Cliente, ClienteAdmin)