# -*- coding: utf-8 -*-

# LIB PARA MANIPULACAO DE PASTAS
import os 
# LIB PARA MANIPULACAO DE ARQUIVOS
import shutil
from django.conf import settings
from django.template.defaultfilters import slugify


def video_post_save(instance, raw, created, **kwargs):
    """Este signal cria uma pasta com o ID do objeto recem criado"""
    if created == True:
        slug = instance.slug
        os.mkdir(os.path.join(settings.MEDIA_ROOT, 'imgs/videos/%s' % slug))

def video_pre_delete(instance, **kwargs):
    """Este signal antes de remover o objeto em sim ele remove a pasta correspondente"""
    slug = instance.slug
    # REMOVE OS ARQUIVOS DA PASTA E A PASTA
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'imgs/videos/%s' % slug))