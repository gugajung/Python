# -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail.fields import ImageField
from sincomercio.parceiros.flags import Status
from sorl.thumbnail.shortcuts import get_thumbnail

class Parceiro(models.Model):      
    nomeRepresentante = models.CharField('Representante', max_length=100)
    imagem = ImageField(upload_to="img")
    visibilidade = models.SmallIntegerField(default=Status.INVISIVEL, choices=Status.ESCOLHAS)
    url = models.URLField(null = True, blank = True)
    
    def image_img(self):
        if self.imagem:
            imagemthumb = get_thumbnail(self.imagem, '150x80', quality=100)        
            return u'<img src="%s" />' % imagemthumb.url        
        else:
            return '(Sem imagem)'
    image_img.short_description = 'Imagem'
    image_img.allow_tags = True
    