#coding:utf-8
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class Anunciante(models.Model):
    anunciante = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='img/anunciantes/')
    link = models.URLField(blank=True, null=True)
    
    def __unicode__(self):
        return self.anunciante
    
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    data = models.DateField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    site = models.URLField(blank=True, null=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    descricao = models.TextField('Descrição')
    imagem = models.ImageField(upload_to='img/eventos/')
    
    def get_absolute_url(self):
        return reverse('matao4x4.views.buscaevento', kwargs={'slug': self.slug})
    
    def __unicode__(self):
        return self.titulo