# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from sincomercio.banners.models import Banner
from sincomercio.campanhas.models import Campanha
from sincomercio.imagens.models import ImagemCampanha

def campanha(request, slug):
    # RETORNA UMA ACAO SOCIAL CASO EXISTA OU UM ERRO 404
    campanha = get_object_or_404(Campanha, slug=slug)
    imagem =  ImagemCampanha.objects.filter(campanha=campanha)[:1]
    # banners do topo lateral direito
    banners_tld = Banner.objects.filter(posicao='tld')
    
    # banners do meio lateral direito
    banners_mld = Banner.objects.filter(posicao='mld')
    
    # banners do baixo lateral direito
    banners_bld = Banner.objects.filter(posicao='bld')
    estilo = "margin-top:40px\9;"
    return render_to_response('ler_campanha.html', locals(),
            context_instance=RequestContext(request))