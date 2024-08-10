# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 08:47:34 2024

@author: merca
"""

print('Ejercicio 6')

class carta:
    
    corazones = 'corazones'
    treboles = 'treboles'
    diamantes = 'diamantes'
    picas = 'picas'
    
    
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta
        
    def mostrar_carta (self):
        print('La carta {} de {}'.format(self.valor, self.pinta)) 
        
mi_carta1 = carta('As', carta.corazones)     
mi_carta2 = carta('Rey', carta.picas)   


mi_carta1.mostrar_carta()
mi_carta2.mostrar_carta()
        
        
      