from ClaseAparato import Aparato

class Televisor(Aparato):
    __tipopantalla =None
    __pulgadas = None
    __TipoDefinicion= None
    __Conexion = bool


    def __init__(self, marca, modelo, color, pais, precio, tipo,pulgadas,definicion,conexion):
        super().__init__(marca, modelo, color, pais, precio)
        self.__tipopantalla = tipo
        self.__pulgadas = pulgadas
        self.__TipoDefinicion = definicion
        self.__Conexion = conexion

    def __str__(self):
        return 'Modelo: {} Marca: {} Color: {} Pais: {} Precio: {} Tipo de pantalla: {} Pulgadas: {} Definicion: {} Conexion a internet: {}\nImporte de venta: {}' .format(super().getMarca(),super().getModelo(), super().getColor(),super().getPaisOrigen(),super().getPrecioBase(),
        self.__tipopantalla, self.__pulgadas, self.__TipoDefinicion, self.__Conexion, super().getImporteVenta())
    
    
    def ImporteVenta(self):
        Importe = 0
        if self.__TipoDefinicion == 'SD':
            Importe+= super().getPrecioBase() + ((1*super().getPrecioBase())/100)
        elif self.__TipoDefinicion == 'HD':
            Importe+= super().getPrecioBase() + ((2*super().getPrecioBase())/100)
        elif self.__TipoDefinicion == 'Full HD':
            Importe+= super().getPrecioBase() + ((3*super().getPrecioBase())/100)
        if self.__Conexion == True:
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
                tipo = self.__tipopantalla,
                pulgadas = self.__pulgadas,
                definicion = self.__TipoDefinicion,
                conexion = self.__Conexion
                )
            )
        return d        
    