# coding: utf-8
'''
Created on 24/08/2011

@author: Matheus
'''

from sincomercio import settings
import os

def deletaImagemComunicado(instance, **kwargs):
    """
        Deleta a imagem do comunicado da pasta
        'comunicados
    """
    if instance.imagem.name:
        caminhoMidias = settings.MEDIA_ROOT
        caminhoImagem = instance.imagem.name
        caminho = os.path.join(caminhoMidias, caminhoImagem)
    
    # remove a imagem da pasta :-)
    os.remove(caminho)
    
