from zooAnimales.animal import Animal

class Reptil(Animal):

    _listado = []
    serpientes = 0
    iguanas = 0
    nReptiles = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.nReptiles += 1
    
    @classmethod
    def cantidadReptiles(clc):
        return clc.nReptiles
    
    def crearIguana(nombre, edad, genero):
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        Reptil.iguanas += 1
        return iguana
    
    def crearSerpiente(nombre, edad, genero):
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        Reptil.serpientes += 1
        return serpiente
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self,colorEscamas):
        self._colorEscamas = colorEscamas
    
    def getLargoCola(self):
        return self._largoCola

    def setLargoCola(self, largoCola):
        self._largoCola = largoCola

    @classmethod
    def getListado(clc):
        return clc._listado 
    
    @classmethod
    def setListado(clc, listado):
        clc._listado = listado
        