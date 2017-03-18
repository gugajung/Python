# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from siteBom.enquetes.models import Enquete

def index(request):
    ultimas_enquetes = Enquete.objects.order_by('-data')

    paginacao = Paginator(ultimas_enquetes, 10)
    
    try:
        pagina = int(request.GET.get('pagina','1'))
    except:
        pagina = 1
    
    try:
        enquetes = paginacao.page(pagina)
    except(EmptyPage, InvalidPage):
        enquetes = paginacao.page(paginacao.num_pages)
        
    return render_to_response('enquetes.html', locals(), context_instance=RequestContext(request))

def enquete(request, slug):
    enquete = get_object_or_404(Enquete, slug=slug)
    return render_to_response('detalhes-enquete.html', locals(), context_instance=RequestContext(request))

def votar(request, slug):
    enquete = get_object_or_404(Enquete, slug=slug)
    
    try:
        opcao_escolhida = enquete.escolha_set.get(pk=request.POST['opcao'])
    except(KeyError, Enquete.DoesNotExist):
        return render_to_response('detalhes-enquete.html',{
                    'enquete': enquete,
                    'mensagem_erro': 'Você não selecionou uma opção',
                }, context_instance=RequestContext(request))
    else:
        opcao_escolhida.votos += 1
        opcao_escolhida.save()
        
        return HttpResponseRedirect(reverse('siteBom.enquetes.views.resultados',
                                       args=(enquete.slug,)))

def resultados(request, slug):
    enquete = get_object_or_404(Enquete, slug=slug)
    return render_to_response('resultados-enquete.html', locals(), context_instance=RequestContext(request))