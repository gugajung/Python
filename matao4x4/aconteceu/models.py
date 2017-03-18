from django.db import models


class Aconteceu(models.Model):
    class Meta:
        ordering = ['titulo']
        verbose_name = ' Acontecimento'
        verbose_name_plural = ' Acontecimentos'
    
    titulo = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.titulo  
    

    @models.permalink
    def get_absolute_url(self):
        return ('matao4x4.views.veraconteceu', [str(self.id)])

class ConteudoAconteceu(models.Model):
    class Meta:
        verbose_name = 'Conteudo Acontecimento'
        verbose_name_plural = 'Conteudo Acontecimentos'
    
    tituloaconteceu = models.ForeignKey(Aconteceu, verbose_name= 'Titulo Aconteceu')
    conteudo = models.TextField()
    
    def __unicode__(self):
        return self.conteudo
    
