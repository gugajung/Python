# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import signals
from sincomercio.extra import ContentTypeRestrictedFileField
from sincomercio.noticias.signals import noticia_post_save, noticia_pre_delete
from sincomercio.utils.signals_comuns import slug_pre_save


escolhas = (
        ('A','Ativada'),
        ('D','Desativada')
    )

class Noticia(models.Model):
    class Meta:
        verbose_name = 'Nova Notícia'
        verbose_name_plural = 'Notícias'
        ordering = ('-data',)
      
    titulo = models.CharField('Título', max_length=100)
    slug = models.SlugField('URL para o site (deixar em branco)', max_length=255, blank=True, unique=True)
    chamada = models.CharField(max_length=255, blank=True)
    conteudo = models.TextField('Conteúdo')
    fonte = models.CharField(max_length=100)
    fonte_url = models.URLField('URL da Fonte', max_length=100, help_text='Exemplo: http://www.nomedosite.com.br/')
    data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=escolhas)
    
    audio = ContentTypeRestrictedFileField(
        'Áudio',
        upload_to='audios/',
        blank=True, null=True,
        content_types=['audio/mpeg','audio/mp3'],
        max_upload_size=31457280 # 30MB
    )
    
    video = models.URLField('URL do vídeo do YouTube', max_length=100, help_text='Exemplo: http://www.youtube.com/embed/obo7QAvaxSU',
                            null=True, blank=True)
    
    def __unicode__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('sincomercio.noticias.views.noticia', kwargs={'slug':self.slug})

class NoticiasTv(models.Model):
    class Meta:
        verbose_name = 'Nova Notícia TV Fecomércio'
        verbose_name_plural = 'Notícias TV Fecomércio'
        ordering = ('-data',)

    titulo = models.CharField('Título',max_length=100)
    slug = models.CharField(max_length=100)
    link = models.URLField(max_length=255, help_text='Link para a notícia com vídeo')
    data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=escolhas)
    
    def __unicode__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('sincomercio.noticias.views.noticiatv', kwargs={'slug':self.slug})

# METODO PARA ADICIONAR AUTOMATICAMENTE UM SLUG        
signals.pre_save.connect(slug_pre_save, sender=Noticia)
#signals.pre_save.connect(slug_pre_save, sender=NoticiasTv)

signals.post_save.connect(noticia_post_save, sender=Noticia)
signals.pre_delete.connect(noticia_pre_delete, sender=Noticia)


#def busca(request):
#    """
#        busca de classe e raca
#    """
#    
#    if request.method == 'POST':
#        
#        tipo = request.POST['id_tipo']
#        id = request.POST[tipo]
#        
#        if(tipo == 'raca'):
#            busca = Raca.buscarRaca(id)
#        else:
#            busca = Classe.buscarClasse(id)
#        
#        json = serializers.serialize("json", busca)
#        return HttpResponse(json, "aplication/json")
#    
#    return HttpResponseRedirect('/');