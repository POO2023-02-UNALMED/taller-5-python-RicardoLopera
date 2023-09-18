from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0
    nAves = 0

    def __init__ (self, nombre, edad, habitat, genero, colorPlumas ):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave.nAves += 1

    @classmethod
    def cantidadAves(clc):
        return Ave.nAves
    
    def crearHalcon(nombre, edad, genero):
        halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        Ave.halcones += 1
        return halcon
    
    def crearAguilas(nombre, edad, genero):
        aguilas = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        Ave.aguilas += 1
        return aguilas
    
    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
    
    @classmethod
    def getListado(clc):
        return clc._listado
    
    @classmethod
    def setListado(clc, listado):
        clc._listado = listado
    
    