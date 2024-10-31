class ReglaValidacion:
    def __init__(longitud_esperada, self):
        self.longitud_esperada = longitud_esperada
        
    def  _validadar_longitud (self, clave):
        return len(clave) > self.longitud_esperada
    
    def _contiene_mayuscula (self, clave):
        return any (c.isupper() for c in clave)
    
    def _contiene_minuscula (self, clave):
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave):
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave):
        return any(c.isdigit() for c in clave)

    @abstractmethod
    def es_valida(self, clave):
        pass
    
    class ReglaValidacionGanimedes:
        
        def __init__(self):
            super()._init__(6)
            
        def _contiene_calisto(self,clave):
            
     def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise Exception("La clave debe tener más de 6 caracteres.")
        if not self._contiene_numero(clave):
            raise Exception("La clave debe contener al menos un número.")
        if not self._contiene_calisto(clave):
            raise Exception("La clave debe incluir 'calisto' con al menos dos letras en mayúscula.")
        
