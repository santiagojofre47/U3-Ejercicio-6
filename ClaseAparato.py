from abc import abstractmethod
from abc import ABC

class Aparato(ABC):
    __marca = None
    __modelo = None
    __color = None
    __pais =  None
    __precio = None
    __importeVenta = None

    def __init__(self,marca,modelo,color,pais,precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__pais = pais
        self.__precio =  precio
        self.__importeVenta = 0

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getColor(self):
        return self.__color

    def getPaisOrigen(self):
        return self.__pais

    def getPrecioBase(self):
        return self.__precio       

    def setImporteVenta(self, Importe):
        self.__importeVenta = Importe

    def getImporteVenta(self):
        return self.__importeVenta                     

    @abstractmethod 
    def ImporteVenta(self):
        pass    
