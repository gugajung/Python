# -*- coding: utf-8 -*-

from PIL import Image
import os
from django import forms
from django.conf import settings
from django.contrib import admin
from sincomercio.banners.models import Banner

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner

class BannerAdmin(admin.ModelAdmin):
    list_display = ('empresa','url', 'posicao', 'tempoExibicao',)
    list_filter = ('empresa',)
    search_fields = ('titulo','descricao',)
    form = BannerForm
    
    def save_model(self, request, obj, form, change):
        super(BannerAdmin, self).save_model(request, obj, form, change)
        
        if 'banner' in form.changed_data:
            nomeImg = obj.banner.name.split('/')[-1]
            pathParcial = 'imgs/banners/%s/%s' %(obj.posicao, nomeImg)
            novoPath = os.path.join(settings.MEDIA_ROOT, pathParcial)
            
            miniatura = Image.open(obj.banner.path)
            novaImg = miniatura.resize((140,125), Image.ANTIALIAS)
            novaImg.save(novoPath)
            
            os.remove(obj.banner.path)
            
            obj.banner = pathParcial
            obj.save()