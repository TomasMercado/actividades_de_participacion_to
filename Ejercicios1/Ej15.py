# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 15:27:38 2024

@author: merca
"""

print('Ejercicio 15')


def palindromo(palabra):
       palabra = palabra.lower()
       return palabra == palabra [::-1]
   
print(palindromo('sol'))
print(palindromo('tomas'))
print(palindromo('ojo'))
