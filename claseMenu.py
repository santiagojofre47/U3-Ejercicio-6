from claseObjectEncoder import ObjectEncoder
from ClaseLista import Lista
from ClaseHeladera import Heladera
from ClaseTelevisor import Televisor
from ClaseLavaropa import Lavaropa

class Menu:
    __opcion = None

    def obtenerAparato(self):
        unAparato = None
        marca = input('Ingrese la marca del aparato: ')
        modelo = input('Ingrese el modelo del aparato: ')
        color = input('Ingrese el color del aparato: ')
        pais = input('Ingrese el pais de origen del aparato: ')
        precio = float(input('Ingrese el precio base del aparato: '))
        correcto = False
        while not correcto:
            print('a- Lavarropa\nb-Televisor\nc-Heladera')
            tipo = input('Ingrese el tipo de aparato: ')
            if tipo.lower() == 'a'.lower():
                correcto = True
                capacidad = int(input('Ingrese la capacidad del lavarropas'))
                velocidad = input('Ingrese la velocidad: ')
                cantidad = int(input('Ingrese la cantidad de programas: '))
                tipo = int(input('Ingrese el tipo de carga 1-Frontal 2- Superior: '))
                tipo_carga = None
                if tipo == 1:
                    tipo_carga = 'Frontal'
                elif tipo == 2:
                    tipo_carga = 'Superior'    
                unAparato = Lavaropa(marca, modelo, color, pais, precio, capacidad, velocidad, cantidad, tipo_carga) 
            elif tipo.lower() == 'b'.lower():
                correcto = True
                tipo_pantalla = input('Ingrese el tipo de pantalla: ')
                pulgadas = float(input('Ingrese la cantidad de pulgadas: '))
                tipo_definicion = input('Ingrese el tipo de definicion: ')
                op = int(input('Posee conexion a internet? 1- Si 2- No: '))
                conexion = None
                if op == 1:
                    conexion = True
                elif op == 2:
                    conexion = False
                unAparato = Televisor(marca, modelo, color, pais, precio, tipo_pantalla, pulgadas, tipo_definicion, conexion) 
            elif tipo.lower() == 'c'.lower():
                correcto = True
                capacidad = int(input('Ingrese la capacidad de la heladera: '))
                op = None
                freezer = None
                ciclica = None
                op = input('Posee freezer? a- si b-no: ')
                if op.lower() == 'a'.lower():
                    freezer = True
                elif op.lower() == 'b'.lower():
                    freezer = False
                op = input('Es ciclico? a- si b- no: ')
                if op.lower() == 'a'.lower():
                    ciclica = True
                elif op.lower() == 'b'.lower():
                    ciclica = False
                unAparato = Heladera(marca, modelo, color, pais, precio, capacidad, freezer, ciclica)
            else:
                print('ERROR: opcion ingresada invalida!')
                input('Presione ENTER para continuar...')
        return unAparato


    def mostrarMenu(self, unaLista, unObjetoEncoder):
        if isinstance(unaLista, Lista) and isinstance(unObjetoEncoder, ObjectEncoder):
            salir = False
            while not salir:
                print('1- Insertar un aparato en la lista en una posicion determinada')
                print('2- Agregar un aparato al final de la lista')
                print('3- Mostrar el tipo de aparato en la posicion de la lista')
                print('4- Mostrar la cantidad de aparatos de la marca Philips registrados')
                print('5- Mostrar la marca de lavarropas con tipo de carga superior')
                print('6- Mostrar los datos de los aparatos')
                print('7- Guardar archivo')
                print('8- Salir')
                self.__opcion = int(input('Ingrese una opcion: '))

                if self.__opcion == 1:
                    aparato = self.obtenerAparato()
                    posicion = int(input('Ingrese la posicion donde se guardara el objeto: '))
                    unaLista.insertarElemento(posicion,aparato)    
                elif self.__opcion == 2:
                    aparato = self.obtenerAparato()
                    unaLista.agregarElemento(aparato)
                elif self.__opcion == 3:
                    posicion = int(input('Ingrese una posicion: '))
                    unaLista.mostrarElemento(posicion)
                elif self.__opcion == 4:
                    cantidad = unaLista.contarPhilips()
                    print('Cantidad de aparatos Philips registrados: {}' .format(cantidad))
                elif self.__opcion == 5:
                    unaLista.mostrarMarcaLavarropaSuperior()
                elif self.__opcion == 6:
                    unaLista.mostrarDatos()
                elif self.__opcion == 7:
                    d = unaLista.toJSON() 
                    unObjetoEncoder.guardarJSONArchivo(d,'aparatoselectronicos.json')
                    print('Archivo guardado con éxito!')
                elif self.__opcion == 8:
                    print('Cerrando menu...')
                    salir = True
                else:
                    print('ERROR: Opcion ingresada invalida!')
                    input('Presione ENTER para continuar...')


   





                            






                            




