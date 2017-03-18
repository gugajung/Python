# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from sincomercio.banners.models import Banner
from sincomercio.imagens.models import ImagemNoticia
from sincomercio.noticias.models import Noticia, NoticiasTv

def noticia(request, slug):
    banners_tld = Banner.objects.filter(posicao='tld')
    banners_mld = Banner.objects.filter(posicao='mld')
    banners_bld = Banner.objects.filter(posicao='bld')

    
    # RETORNA UMA NOTICIA CASO EXISTA OU UM ERRO 404
    noticia = get_object_or_404(Noticia, slug=slug)
    imagem =  ImagemNoticia.objects.filter(noticia=noticia)[:1]
    imagens =  ImagemNoticia.objects.filter(noticia=noticia)
    
    estilo = "margin-top:40px\9;"
    
    return render_to_response('ler_noticia.html', locals(),
            context_instance=RequestContext(request))

def noticiatv(request,slug):
    noticia = get_object_or_404(NoticiasTv, slug=slug)
    link = noticia.link
    
    return redirect(link)