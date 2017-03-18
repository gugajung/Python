#coding:utf-8
"""
Models do módulo de clientes.
"""

from django.contrib.admin.models import User
from django.db import models

SEXO = (
            ('M', 'Masculino'),
            ('F','Feminino'),
            )

class Cliente(User):
    """
    Classe que representa um Cliente    
    """
    
    telefone = models.CharField(blank = True, null = True,max_length = 55)
    endereco = models.CharField(blank = True, null = True, max_length = 55)

#--
    
    