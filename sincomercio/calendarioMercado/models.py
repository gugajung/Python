# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import signals
from sincomercio.banners.signals import banner_post_save
from sincomercio.calendario.flags import Datas

class CalendarioMercado(models.Model):    
    dataInicial = models.DateField('DataInicial')
    dataFinal = models.DateField('DataFinal')
    horaInicio = models.TimeField('Horario Inicial')
    horaFinal = models.TimeField('Horario Final')
    ocasiao = models.SmallIntegerField('Ocasião', choices=Datas.ESCOLHAS)
    motivo = models.CharField('Motivo', max_length=50)
    
    def __unicode__(self):
        return self.motivo