# -*- coding: utf-8 -*-

# LIB PARA MANIPULACAO DE PASTAS
import os 
# LIB PARA MANIPULACAO DE ARQUIVOS
import shutil
from django.conf import settings
from django.template.defaultfilters import slugify


def loja_post_save(instance, raw, created, **kwargs):
    """Este signal cria uma pasta com o ID do objeto recem criado"""
    if created == True:
        id = instance.id
        os.mkdir(os.path.join(settings.MEDIA_ROOT, 'imgs/lojas/%d' % id))

def loja_pre_delete(instance, **kwargs):
    """Este signal antes de remover o objeto em sim ele remove a pasta correspondente"""
    id = instance.id
    # REMOVE OS ARQUIVOS DA PASTA
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'imgs/lojas/%d' % id))