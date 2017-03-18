from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import signals
from siteBom.enquetes.signals import slug_pre_save

# Create your models here.

class Dica(models.Model):
    class Meta:
        verbose_name = 'dica'
        verbose_name_plural = 'Dicas'
        
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    texto = models.TextField('Dica')
    data = models.DateField(auto_now_add=True,blank=True)
    
    def __unicode__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('siteBom.dicas.views.dica', kwargs={'slug':self.slug})

signals.pre_save.connect(slug_pre_save, sender=Dica)