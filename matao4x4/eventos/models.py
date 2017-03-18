from django.db.models import signals
from django.db import models
from sorl.thumbnail.fields import ImageField
from django.template.defaultfilters import default


escolhas =(
       ('0','Nao'),
       ('1','Sim'),    
      )

class Eventos(models.Model):
    class Meta:
        ordering = ('titulo',)
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    titulo = models.CharField('Titulo', blank=True, max_length=100)

    def __unicode__(self):
        return self.titulo
    

class GaleriaEvento(models.Model):

    evento = models.ForeignKey(Eventos)

    def __unicode__(self):
        return 'GaleriaEvento '
    
    
class ImagemGaleria(models.Model):
    
    galeriaEvento = models.ForeignKey(GaleriaEvento, related_name='imagens')
    imagem = ImageField(upload_to="img/galeria")
    capa = models.CharField(max_length=1, choices=escolhas, default= 0)

    def __unicode__(self):
        return 'ImagemGaleria'
  
