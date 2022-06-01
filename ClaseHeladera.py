import json
from ClaseAparato import Aparato
class Heladera(Aparato):
    __capacidad = None
    __freezer = bool
    __ciclica = bool

    def __init__(self, marca, modelo, color, pais, precio,capacidad,freezer,ciclicla):
        super().__init__(marca, modelo, color, pais, precio)
        self.__capacidad = capacidad 
        self.__freezer = freezer
        self.__ciclica = ciclicla

    def __str__(self):
        return 'Modelo: {} Marca: {} Color: {} Pais: {} Precio: {} Capacidad: {} Freezer: {} Ciclica: {}\nImporte de venta: {}' .format(super().getMarca(),super().getModelo(), super().getColor(),super().getPaisOrigen(),super().getPrecioBase(),
        self.__capacidad, self.__freezer, self.__ciclica, super().getImporteVenta())
         
    def ImporteVenta(self):
        Importe = 0
        if self.__freezer == True:
            Importe+= super().getPrecioBase() + ((5*super().getPrecioBase())/100)
        else:
            Importe+= super().getPrecioBase() + ((1*super().getPrecioBase())/100)
        if self.__ciclica == True:
            Importe+= super().getPrecioBase() + ((10*super().getPrecioBase())/100)

        super().setImporteVenta(Importe)          

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                marca = super().getMarca(),
                modelo = super().getModelo(),
                color = super().getColor(),
                pais = super().getPaisOrigen(),
                precio = super().getPrecioBase(),
               # importeVenta = super().getImporteVenta(),
                capacidad = self.__capacidad,
                freezer = self.__freezer,
                ciclicla = self.__ciclica
                )
            )
        return d        

        