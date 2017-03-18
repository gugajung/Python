# Create your views here.
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from siteBom.dicas.models import Dica

def index(request):
    ultimas_dicas = Dica.objects.order_by('-data')

    paginacao = Paginator(ultimas_dicas, 10)
    
    try:
        pagina = int(request.GET.get('pagina','1'))
    except:
        pagina = 1
    
    try:
        dicas = paginacao.page(pagina)
    except(EmptyPage, InvalidPage):
        dicas = paginacao.page(paginacao.num_pages)
    
    return render_to_response('dicas.html',locals(),context_instance=RequestContext(request))

def dica(request,slug):
    dica = get_object_or_404(Dica, slug=slug)
    return render_to_response('detalhes-dicas.html',locals(),context_instance=RequestContext(request))