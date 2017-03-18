# -*- coding: utf-8 -*-

# LIB PARA MANIPULACAO DE PASTAS
from django.conf import settings
from sincomercio.imagens.signals import limparPastaImagens
import glob
import os
import shutil
# LIB PARA MANIPULACAO DE ARQUIVOS

def campanha_post_save(instance, raw, created, **kwargs):
    limparPastaImagens(os.path.join(settings.MEDIA_ROOT,'imgs/campanhas/%d/' % instance.id))
    limparPastaImagens(os.path.join(settings.MEDIA_ROOT,'imgs/campanhas/menores/%d/' % instance.id))
    
    if created == True:
        os.mkdir(os.path.join(settings.MEDIA_ROOT, 'imgs/campanhas/%d' % instance.id))
        os.mkdir(os.path.join(settings.MEDIA_ROOT, 'imgs/campanhas/menores/%d' % instance.id))

def campanha_pre_delete(instance, **kwargs):
    id = instance.id
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'imgs/campanhas/%d/' % id))
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'imgs/campanhas/menores/%d/' % id))