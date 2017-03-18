'''
Created on 27/10/2010

@author: Matheus
'''
from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.db.models.fields.files import FileField, FileDescriptor, FieldFile
from django.utils.translation import ugettext_lazy

def cria_paginacao(request, lista):
    paginacao = Paginator(lista, 12)

    try:
        pagina = int(request.GET.get('pagina','1'))
    except:
        pagina = 1
    
    try:
        paginas = paginacao.page(pagina)
    except(EmptyPage, InvalidPage):
        paginas = paginacao.page(paginacao.num_pages)
    
    return paginas