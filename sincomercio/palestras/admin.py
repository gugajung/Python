# -*- coding: utf-8 -*-
import os
import shutil
from PIL import Image
from django import forms
from django.conf import settings
from django.contrib import admin
from sincomercio.noticias.models import Noticia
from sincomercio.noticias.models import NoticiasTv
from sincomercio.imagens.models import ImagemNoticia
from sincomercio.palestras.models import Plestras


class PalestrasAdmin(admin.ModelAdmin):
    list_display = ('titulo','data', 'texto')
    list_filter = ('data',)
    search_fields = ('titulo','data',)
    
admin.site.register(Plestras, PalestrasAdmin)
