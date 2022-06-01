from ClaseAparato import Aparato
class Lavaropa(Aparato):
    __capacidad = None
    __velocidad = None
    __cantidad = None
    __tipocarga  = None

    def __init__(self, marca, modelo, color, pais, precio,capacidad,velocidad,cantidad,tipocarga):
        super().__init__(marca, modelo, color, pais, precio)
        self.__capacidad = capacidad
        self.__velocidad = velocidad
        self.__cantidad = cantidad
        self.__tipocarga = tipocarga

    def __str__(self):
        return 'Modelo: {} Marca: {} Color: {} Pais: {} Precio: {} Capacidad: {} Velocidad: {} Cantidad: {} Tipo de carga: {}\nImporte de venta: {}' .format(super().getMarca(),super().getModelo(), super().getColor(),super().getPaisOrigen(),super().getPrecioBase(),
        self.__capacidad, self.__velocidad, self.__cantidad, self.__tipocarga, super().getImporteVenta())

    def getTipoCarga(self):
        return self.__tipocarga    
    
    def ImporteVenta(self):
        Importe = 0
        if self.__capacidad <= 5:
            Importe+= super().getPrecioBase() + ((1*super().getPrecioBase())/100)
        else:
            Importe+= super().getPrecioBase() + ((3*super().getPrecioBase())/100)
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
                velocidad = self.__velocidad,
                cantidad = self.__cantidad,
                tipocarga = self.__tipocarga
                )
            )
        return d        