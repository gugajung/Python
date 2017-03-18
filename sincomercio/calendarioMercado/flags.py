'''
Created on 05/07/2012

@author: Administrador
'''

class Datas():
    ABERTO = 0
    ABERTOESPECIAL = 1
    FECHADO = 2
    
    ESCOLHAS = (
        (ABERTO, "Comercio Aberto"),
        (ABERTOESPECIAL, "Comercio Aberto Horario Especial"),
        (FECHADO, "Comercio Fechado"),
    )