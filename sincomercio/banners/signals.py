#-*- coding: utf-8 -*-

# LIB PARA MANIPULACAO DE PASTAS
import os 
# LIB PARA MANIPULACAO DE IMAGENS
from PIL import Image
from django.conf import settings
from django.template.defaultfilters import slugify


def banner_post_save(instance, raw, created, **kwargs):
    """Este signal cria uma pasta com o ID da not�cia recem criada"""
    if created == True:
    	nomeImg = instance.banner.name.split('/')[-1]

       
