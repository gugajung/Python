# coding: utf-8
from PIL import Image
from django import forms
from django.conf import settings
from django.contrib import admin
from django.utils.encoding import smart_str, smart_unicode
from sincomercio.videoteca.models import Genero, Videoteca
from unicodedata import normalize
import md5
import os

class FormVideo(forms.ModelForm):
    model = Videoteca

class AdminVideo(admin.ModelAdmin):
    fieldsets = (
        ('Sobre o Vídeo',
         {'fields':('titulo', 'codigo', 'genero', 'status', 'capa', 'ano')
        }),
    )
    list_display = ('titulo', 'ano', 'genero', 'status', 'data')
    
    list_filter = ('titulo', 'ano')
    
    search_fields = ('titulo', 'ano', 'genero', 'codigo')

    def save_model(self, request, obj, form, change):
        super(AdminVideo, self).save_model(request, obj, form, change)
        
        if 'capa' in form.changed_data:
            nomeImg = obj.capa.name.split('/')[-1]
            ext = nomeImg.split('.')[1]
            
            hash = md5.new()
            hash.update(smart_str(unicode(nomeImg)))
            
            nomeImg = hash.hexdigest() + '.' + ext
        
            pathOriginal = os.path.join(settings.MEDIA_ROOT, 'imgs/videos/%s/%s' % (obj.slug, nomeImg))
            pathParcial = 'imgs/videos/%s/min_%s' % (obj.slug, nomeImg)
            novoPath = os.path.join(settings.MEDIA_ROOT, pathParcial)
            
            miniatura = Image.open(obj.capa.path)
            novaImg = miniatura.resize((96, 87), Image.ANTIALIAS)
            novaImg.save(novoPath)
            
            # CRIANDO UMA NOVA CAPA
            nova_capa = Image.open(obj.capa.path)
            #            nova = nova_capa.resize((335,543), Image.ANTIALIAS)
            nova = nova_capa.resize((1000, 680), Image.ANTIALIAS)
            nova.save(pathOriginal)
            
            # REMOVE A IMAGEM ANTIGA
            os.remove(obj.capa.path)
            
            obj.capa = 'imgs/videos/%s/%s' % (obj.slug, nomeImg)
            obj.capa_menor = pathParcial
            
            gen = obj.genero
            
            genero = Genero.objects.get(nome=gen)
            genero.num_filmes = genero.num_filmes + 1
            
            genero.save()
            obj.save()

class AdminGenero(admin.ModelAdmin):
    fieldsets = (
        ('Gênero',
        {'fields':('nome',)
        }),
    )

    def save_model(self, request, obj, form, change):
        super(AdminGenero, self).save_model(request, obj, form, change)
        
        obj.num_filmes = 0
        obj.save()



admin.site.register(Videoteca, AdminVideo)
admin.site.register(Genero, AdminGenero)
