# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import signals
from django.core.urlresolvers import reverse
from siteBom.enquetes.signals import slug_pre_save

# Create your models here.
class Enquete(models.Model):
    class Meta:
        verbose_name = 'enquete'
        verbose_name_plural = 'Enquetes'
        
    titulo = models.CharField('Pergunta', max_length=200,
                              help_text='Não é necessário colocar "?" no final. :-)')
    slug = models.CharField(max_length=200)
    data = models.DateTimeField('Data', auto_now_add=True)
    
    def __unicode__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('siteBom.enquetes.views.enquete', kwargs={'slug':self.slug})

class Escolha(models.Model):
    class Meta:
        verbose_name = 'Opção'
        verbose_name_plural = 'Opções'
        
    enquete = models.ForeignKey(Enquete)
    escolha = models.CharField('Opção', max_length=200)
    votos = models.IntegerField()
    
    def __unicode__(self):
        return self.escolha

 
signals.pre_save.connect(slug_pre_save, sender=Enquete)