# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 15:25:00 2024

@author: merca
"""

print('Ejercicio 14')

def calcular_media(lista):
    if len(lista) == 0:
        return 0
    
    suma = sum(lista)
    
    media = suma / len(lista)
    
    return media

numeros = [1, 2, 3, 4, 5]
media = calcular_media(numeros)
print("La media aritmética es:", media)