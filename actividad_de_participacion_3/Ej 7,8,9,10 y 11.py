# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 08:58:08 2024

@author: merca
"""

print('Ejericio 7,8,9,10,11')

class cuenta_bancaria:
    
    
    def __init__(self,numero_cuenta,propietarios,balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
        
    def mostra_cuenta (self):
        print('Bienvenido {} su numero de cuenta es {} el balace es {}'.format(self.numero_cuenta,self.propietarios,self.balance))
    
    def depositar (self):
        self.tot = self.balance + 20000000
        print('ahora cuenta con un balance de {}'.format(self.tot))
        
    def retirar (self):
        self.re = self.tot - 2000
        print('Haz retrado dinero tu balance actual es de {}'.format(self.re))
        
    def aplicar_cuota (self):
        self.cuo = self.balance * 0.02
        print('Su balance con cuota aplicada del 2% es de {}'.format(self.cuo))
        
    def mostrar_detalles (self):
        print('Detalles de cuenta bancaria:')
        print('Numero de cuenta: {}'.format(self.numero_cuenta))
        print('Propietarios: {}'.format(self.propietarios))
        print('El balance : {}'.format(self.balance))
        
    
        

mi_cuenta = cuenta_bancaria(123456789, 'Tomas Mercado', 100000) 
      

mi_cuenta.mostra_cuenta()
mi_cuenta.depositar()
mi_cuenta.retirar()
mi_cuenta.aplicar_cuota()
mi_cuenta.mostrar_detalles()

   
