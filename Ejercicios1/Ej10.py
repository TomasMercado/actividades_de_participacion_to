# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 09:44:14 2024

@author: merca
"""

print('Ejercicio 10')

n= int(input('Digite el numero al cual le quiere sacar factorial: '))
fact=1
for i in range(1,n+1):
    fact*=i
print('El resultado es: ',fact)    