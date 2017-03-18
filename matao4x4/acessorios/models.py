#-*- coding:utf-8 -*-
from django.db import models
from django.utils.formats import number_format

# Create your models here.

class MarcaAcessorio(models.Model):
    class Meta:
        verbose_name_plural = 'Marca de Acessórios'
    nome = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.nome
    
class TipoAcessorio(models.Model):
    tipo = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.tipo
    
class Acessorio(models.Model):

    marca = models.ForeignKey(MarcaAcessorio)
    tipo = models.ForeignKey(TipoAcessorio)
    nome = models.CharField(max_length=100)
    descricao = models.TextField('Descrição')
    valor = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
#    unidade = models.CharField(max_length=15, blank=True, null=True)
    email_contato = models.EmailField('E-mail para contato', max_length=120, blank=True, null=True)
        
    def __unicode__(self):
        return self.nome
    
    def valor_formatado(self):
        return u"R$ %s" % number_format(self.valor, 2) #Formata o campo para moeda brasileira

    def obterFoto(self):
        return self.fotosacessorio_set.get(acessorio = self, capa = 1)
    
    def obterFotos(self):
        return self.fotosacessorio_set.filter(acessorio = self)
        
        
        
class FotosAcessorio(models.Model):
    class Meta:
        verbose_name_plural = 'Fotos Acessórios'
    acessorio = models.ForeignKey(Acessorio)
    foto = models.ImageField(upload_to='img/acessorios/')
    capa = models.IntegerField(choices=( (1, 'Sim'), (0, 'Não')), default=0)

    def __unicode__(self):
        return self.foto.name

