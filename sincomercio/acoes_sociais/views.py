# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from sincomercio.acoes_sociais.models import AcaoSocial
from sincomercio.banners.models import Banner
from sincomercio.imagens.models import ImagemAcoesSociais

def acao(request, slug):
    # RETORNA UMA ACAO SOCIAL CASO EXISTA OU UM ERRO 404
    acao = get_object_or_404(AcaoSocial, slug=slug)
    imagem =  ImagemAcoesSociais.objects.filter(acao=acao)[:1]
    imagens =  ImagemAcoesSociais.objects.filter(acao=acao)
    # banners do topo lateral direito
    banners_tld = Banner.objects.filter(posicao='tld')
    
    # banners do meio lateral direito
    banners_mld = Banner.objects.filter(posicao='mld')
    
    # banners do baixo lateral direito
    banners_bld = Banner.objects.filter(posicao='bld')
    estilo = "margin-top:40px\9;"
    return render_to_response('ler_acao_social.html', locals(),
            context_instance=RequestContext(request))