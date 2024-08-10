# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 06:09:51 2024

@author: merca
"""

print('Ejercicio 1')
class vehiculo:
    def __init__(self, maxima_velocidad, kilometraje):
        self.maxima_velocidad =maxima_velocidad
        self.kilometraje = kilometraje
        
mi_vehiculo= vehiculo( 140 , 370.000)
print(mi_vehiculo.maxima_velocidad)
print(mi_vehiculo.kilometraje)
