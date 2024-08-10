# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 21:30:51 2024

@author: merca
"""

print('Ejercicio 4')

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangulo:
    def __init__(self, esquina1, esquina2):
        self.esquina1 = esquina1
        self.esquina2 = esquina2

    def calcular_lados(self):
        base = abs(self.esquina1.x - self.esquina2.x)
        altura = abs(self.esquina1.y - self.esquina2.y)
        return base, altura

    def area(self):
        base, altura = self.calcular_lados()
        area = base * altura
        return area

    def perimetro(self):
        base, altura = self.calcular_lados()
        perimetro = 2 * (base + altura)
        return perimetro

    def identificar(self):
        base, altura = self.calcular_lados()
        if base == altura:
            print('La figura es un cuadrado')
        else:
            print('La figura es un rectángulo')


esquina1 = Punto(4, 6)
esquina2 = Punto(10, 12)

mi_rectangulo = Rectangulo(esquina1, esquina2)

print(f"Área del rectángulo: {mi_rectangulo.area()}")

print(f"Perímetro del rectángulo: {mi_rectangulo.perimetro()}")


mi_rectangulo.identificar()
        
        