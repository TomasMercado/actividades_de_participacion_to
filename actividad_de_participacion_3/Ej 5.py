# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 06:45:43 2024

@author: merca
"""

print('Ejercicio 5')

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
    
    def area(self):
        area = 3.1416 * (self.radio ** 2)
        print(f"El área del círculo es: {area}")
    
    def perimetro(self):
        perimetro = 2 * 3.1416 * self.radio
        print(f"El perímetro del círculo es: {perimetro}")
    
    def pertenece_al_circulo(self, punto):
        distancia = ((punto.x - self.centro.x) ** 2 + (punto.y - self.centro.y) ** 2) ** 0.5
        if distancia <= self.radio:
            print("El punto pertenece al círculo")
        else:
            print("El punto no pertenece al círculo")


centro = Punto(0, 0)
mi_circulo = Circulo(centro, 5)
mi_circulo.area()
mi_circulo.perimetro()
punto = Punto(3, 4)
mi_circulo.pertenece_al_circulo(punto)