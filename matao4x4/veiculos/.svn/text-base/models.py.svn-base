#-*-coding: utf-8 -*-
from django.db import models

# Create your models here.

class MarcaCarro(models.Model):
    nome = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.nome

class Veiculos(models.Model):
    
    class Meta:
        verbose_name_plural = 'Veiculos'
    
    marca = models.ForeignKey(MarcaCarro)   
    modelo = models.CharField(max_length=100)
    descricao = models.TextField('Descrição')
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def __unicode__(self):
        return self.modelo
    
    def obterFoto(self):
        return self.fotosveiculo_set.get(veiculo = self, capa = 1).foto
    
    def obterFotos(self):
        return self.fotosveiculo_set.filter(veiculo = self)
    
class FotosVeiculo(models.Model):
    class Meta:
        verbose_name_plural = 'Fotos Veículos'
    veiculo = models.ForeignKey(Veiculos)
    foto = models.ImageField(upload_to='img/veiculos/')
    capa = models.IntegerField(choices = ( (1, 'Sim'), (0, 'Não')), null=True, blank=True, default = 0)
    
    def __unicode__(self):
        return 'FotosAcessorios {0}'.format(self.id)
