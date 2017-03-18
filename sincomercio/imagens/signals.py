# -*- coding: utf-8 -*-

# LIB PARA MANIPULACAO DE PASTAS
import os, glob
# LIB PARA MANIPULACAO DE ARQUIVOS
import shutil
# LIB PARA MANIPULACAO DE IMAGENS
from PIL import Image
from django.conf import settings
from django.template.defaultfilters import slugify

def criarThumbnail(original, novoPath):
    """
        Cria um thumbnail de uma imagem maior
    """
    miniatura = Image.open(original, 'r')
    
    if miniatura: 
        miniatura.thumbnail( (122,91) , Image.ANTIALIAS)
#        novaImg = miniatura.resize((122,91), Image.ANTIALIAS)
        miniatura.save(novoPath)
    else:
        print "NAO CRIOU THUMBNAIL"

def redimensionaImg(original, novoPath):
    """
        Cria uma nova imagem com um novo tamanho
    """
    img_normal = Image.open(original)
    novaImg = img_normal.resize((640,480), Image.ANTIALIAS)
    novaImg.save(novoPath)

def limparPastaImagens(pasta):
    """
        Limpa todas as imagens, de qualquer formato,
        da pasta indicada
    """
    print "PASTA A SER DELETADA: ", pasta
    if os.path.exists(pasta):
        for arquivo in glob.glob(pasta + "/*.jpg"):
            os.unlink(arquivo)

def getNomeImagem(imagem):
    """
        Retorna o nome da imagem em minusculo
    """
    return imagem.split('/')[-1].lower()

def imagem_acao_post_save(instance, raw, created, **kwargs):
    """
        Tratamento das imagens após o envio de uma nova campanha
    """
    if created:
        dir(instance)
    else:
        dir(instance)
    
    id = instance.acao.id
       
    nomeImagem = getNomeImagem(instance.foto_acao.name)
    
    dirImagemEnviada = os.path.join(settings.MEDIA_ROOT, 'imgs/acoes_sociais/%s' % nomeImagem)
    
    dirNomeImgMenor = 'imgs/acoes_sociais/menores/%d/min_%s'
    dirNomeImgMaior = 'imgs/acoes_sociais/%d/%s'
    
    dirImagemMenor =  os.path.join(settings.MEDIA_ROOT, dirNomeImgMenor % (id, nomeImagem))
    dirImagemMaior =   os.path.join(settings.MEDIA_ROOT, dirNomeImgMaior % (id, nomeImagem)) 
    
    if os.path.exists(dirImagemEnviada):
        
        criarThumbnail(dirImagemEnviada, dirImagemMenor)
        redimensionaImg(dirImagemEnviada, dirImagemMaior)
        os.unlink(dirImagemEnviada)
    
        instance.foto_acao = dirNomeImgMaior % (id, nomeImagem)
        instance.foto_acao_menor = dirNomeImgMenor % (id, nomeImagem)
        instance.save()

def imagem_campanha_post_save(instance, raw, created, sender, **kwargs):
    """
        Tratamento das imagens após o envio de uma nova campanha
    """
    
    id = instance.campanha_id
       
    nomeImagem = getNomeImagem(instance.fotoCamp.name)
    
    dirImagemEnviada = os.path.join(settings.MEDIA_ROOT, 'imgs/campanhas/%s' % nomeImagem)
    
    dirNomeImgMenor = 'imgs/campanhas/menores/%d/min_%s'
    dirNomeImgMaior = 'imgs/campanhas/%d/%s'
    
    dirImagemMenor =  os.path.join(settings.MEDIA_ROOT, dirNomeImgMenor % (id, nomeImagem))
    dirImagemMaior =   os.path.join(settings.MEDIA_ROOT, dirNomeImgMaior % (id, nomeImagem)) 
    
    if os.path.exists(dirImagemEnviada):
        
        criarThumbnail(dirImagemEnviada, dirImagemMenor)
        redimensionaImg(dirImagemEnviada, dirImagemMaior)
        os.unlink(dirImagemEnviada)
    
        instance.fotoCamp = dirNomeImgMaior % (id, nomeImagem)
        instance.fotoCampMenor = dirNomeImgMenor % (id, nomeImagem)
        instance.save()