# -*- coding: utf-8 -*-
import os
import shutil
from PIL import Image
from django.contrib import admin
from django.conf import settings
from sincomercio.loja_aniver.models import LojaAniver

class AdminLojaAniver(admin.ModelAdmin):
    fieldsets = (
       ('Sobre a Loja Aniversariante',
        {'fields':('nome','descricao','data_aniver', 'foto_loja')
        }),             
    )
    list_display = ('nome','descricao','data_aniver',)

    list_filter = ('nome',)
    search_fields = ('nome','descricao',)
    
    def save_model(self, request, obj, form, change):
        super(AdminLojaAniver, self).save_model(request, obj, form, change)
        
        if 'foto_loja' in form.changed_data:
            nomeImg = obj.foto_loja.name.split('/')[-1]
            pathParcial = 'imgs/lojas/%d/min_%s' %(obj.id, nomeImg)
            pathImgNormalParcial = 'imgs/lojas/%d/%s' % (obj.id, nomeImg)
            novoPath = os.path.join(settings.MEDIA_ROOT, pathParcial)
            novoPathImgNormal = os.path.join(settings.MEDIA_ROOT, pathImgNormalParcial)
            
            miniatura = Image.open(obj.foto_loja.path)
            novaImgMin = miniatura.resize((128,93), Image.ANTIALIAS)
            novaImgMin.save(novoPath)
            
            img_normal = Image.open(obj.foto_loja.path)
            novaImg = img_normal.resize((640,480), Image.ANTIALIAS)
            novaImg.save(novoPathImgNormal)
            
#           shutil.move(obj.capa.path, os.path.join(settings.MEDIA_ROOT, 'imgs/lojas/%d/' % obj.id))
            os.remove(obj.foto_loja.path)
            
            obj.foto_loja = pathImgNormalParcial
            obj.foto_loja_menor = pathParcial
            obj.save()
    
admin.site.register(LojaAniver, AdminLojaAniver)