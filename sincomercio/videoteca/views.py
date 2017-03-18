# -*- coding: utf-8 -*-
from django.core import serializers
from django.http import HttpResponse
#from django.shortcuts import render_to_response, get_object_or_404
#from django.template import RequestContext
#from sincomercio.generos.models import Genero
#from sincomercio.utils.auxiliares import cria_paginacao
from sincomercio.videoteca.models import Videoteca

def info_video(request, video_id):
    info = Videoteca.objects.filter(id=video_id)
    retorno = serializers.serialize("json", info, indent=2, use_natural_keys=True)
    return HttpResponse(retorno, mimetype="application/json")    