# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from sincomercio.banners.models import Banner
from sincomercio.imagens.models import ImagemNoticia
from sincomercio.noticias.models import Noticia, NoticiasTv
from sincomercio.palestras.models import Plestras
from django.utils.datetime_safe import date

    
