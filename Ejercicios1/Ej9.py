# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 09:34:05 2024

@author: merca
"""

print('Ejercicio 9')
import random
L=[0]
f=int(input('Digite el numero de filas que tendra la matriz '))
c=int(input('Digite el numero de columnas que tendra la matriz '))
for i in range(f):
    for j in range(c):
        L.append(random.randint(0, 30))
print(L)    