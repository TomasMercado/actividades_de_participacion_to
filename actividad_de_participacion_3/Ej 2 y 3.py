# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 06:23:29 2024

@author: merca
"""

print('Ejercicio 2,3')

from math import sqrt

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar_coordenadas(self):
        print("Las coordenadas del punto son: x:{} y:{}".format(self.x, self.y))
        
    def nuevas_coordenadas(self, nueva_x, nueva_y):
        self.x = nueva_x
        self.y = nueva_y

    def distancia_entre_puntos(self, otro_punto):
        distancia = sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)
        print(f"La distancia entre los puntos es: {distancia:.2f}")


mi_punto = Punto(6, 8)
mi_otro_punto = Punto(10, 18)
mi_punto.mostrar_coordenadas()
mi_otro_punto.mostrar_coordenadas()
mi_punto.distancia_entre_puntos(mi_otro_punto)
mi_punto.nuevas_coordenadas(10, 20)
mi_punto.mostrar_coordenadas()
mi_punto.distancia_entre_puntos(mi_otro_punto)