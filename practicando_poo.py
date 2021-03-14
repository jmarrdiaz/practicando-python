"""
class Moto:
    
    concesionario = "Chafiras Motos S.L"
    
    def __init__(self, ruedas, color, modelo, chasis):
        self.ruedas = ruedas
        self.color = color
        self.modelo = self.toList(modelo)
        self.__chasis = chasis
    
    @property
    def getChasis(self):
        return self.__chasis
    
    def toList(self, value):
        return list(value)
    
moto = Moto(4, 'blanco', 'BMW', 'fsdafas')

print(moto.getChasis)
print(moto.modelo)

"""

class Moto:
    concesionario = "Chafiras SL"
    def __init__(self, color, marca, modelo, chasis):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.__chasis = chasis
    
    @property
    def getChasis(self):
        return self.__chasis
    
moto = Moto('blanco', 'Suzuki', 'GSX-R', 'sdfsd')

print(moto.concesionario)