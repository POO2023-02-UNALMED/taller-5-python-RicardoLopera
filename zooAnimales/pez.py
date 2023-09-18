from zooAnimales.animal import Animal

class Pez(Animal):
    
    _listado = []
    salmones = 0
    bacalaos = 0
    nPeces = 0

    def __init__(self, nombre, edad, habitad, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitad, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez.nPeces += 1

    @classmethod
    def cantidadPeces(cls):
        return cls.nPeces
    
    def crearSalmon(nombre, edad, genero):
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        Pez.salmones += 1
        return salmon
    
    def crearBacalao(nombre, edad, genero):
        bacalao = Pez(nombre, edad, "oceano", genero, "gris",6)
        Pez.bacalaos += 1
        return bacalao
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas
    
    @classmethod 
    def getListado(clc):
        return clc._listado
    
    @classmethod
    def setListado(clc, listado):
        clc._listado = listado
    