# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import signals
from sincomercio.banners.signals import banner_post_save

class Banner(models.Model):
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
        
    posicoes = (
      ('tld','Topo Lateral Direito'),
      ('mld','Meio Lateral Direito'),
      ('bld','Baixo Lateral Direito'),
    )
    
    # TAMANHO DO BANNER: 140x125
    
    empresa = models.CharField('Anunciante', max_length = 100)
    url = models.URLField('URL do Site', max_length = 100, 
    help_text = 'URL para o site do anunciante. Formato de uma URL: http://www.exemplo.com.br/')
    posicao = models.CharField('Posição', max_length = 3, choices = posicoes)
    tempoExibicao = models.IntegerField('Tempo de exibição', help_text = 'Tempo de exibição em segundos')
    banner = models.ImageField(upload_to= 'imgs/banners/', help_text = 'Imagem irá ser redimensionada para 140x125.')
    
    def __unicode__(self):
        return self.empresa

signals.post_save.connect(banner_post_save, sender=Banner)