# -*- coding: utf-8 -*-

# LIB PARA MANIPULACAO DE PASTAS
import os 
# LIB PARA MANIPULACAO DE ARQUIVOS
import shutil
# LIB PARA MANIPULACAO DE IMAGENS
from PIL import Image
from django.conf import settings
from django.template.defaultfilters import slugify


def noticia_post_save(instance, raw, created, **kwargs):
    """Este signal cria uma pasta com o ID da notícia recem criada"""
    if created == True:
        id = instance.id
        print 'SETTINGS MEDIA ROOT: ' + os.path.join(settings.MEDIA_ROOT,('imgs/noticias/%d' % id))
        os.mkdir(os.path.join(settings.MEDIA_ROOT, 'imgs/noticias/%d' % id))

def noticia_pre_delete(instance, **kwargs):
    """Este signal antes de remover ele remove a pasta da noticia"""
    id = instance.id
    # REMOVE OS ARQUIVOS DA PASTA E A PASTA
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'imgs/noticias/%d/' % id))