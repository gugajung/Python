# -*- coding: utf-8 -*-

# LIB PARA MANIPULACAO DE PASTAS
import os 
# LIB PARA MANIPULACAO DE ARQUIVOS
import shutil
from django.conf import settings


def acao_post_save(instance, raw, created, **kwargs):
    """Este signal cria uma pasta com o ID da not�cia recem criada"""
    if created == True:
        id = instance.id
        os.mkdir(os.path.join(settings.MEDIA_ROOT, 'imgs/acoes_sociais/%d' % id))
        os.mkdir(os.path.join(settings.MEDIA_ROOT, 'imgs/acoes_sociais/menores/%d' % id))

def acao_pre_delete(instance, **kwargs):
    """Este signal antes de remover ele remove a pasta da noticia"""
    id = instance.id
    # REMOVE OS ARQUIVOS DA PASTA E A PROPRIA PASTA
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'imgs/acoes_sociais/%d/' % id))
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'imgs/acoes_sociais/menores/%d/' % id))