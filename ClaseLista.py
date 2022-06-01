from ClaseNode import Nodo
from ClaseAparato import Aparato
from ClaseHeladera import Heladera
from ClaseLavaropa import Lavaropa
from ClaseTelevisor import Televisor
from zope.interface import implementer
from Interface import iInterface

@implementer(iInterface)

class Lista:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0

    def __init__(self):
        self.__comienzo=None
        self.__actual=None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def toJSON(self):
        d = dict(__class__ = self.__class__.__name__,
        Aparatos = [aparatos.toJSON() for aparatos in self]
        )
        return d
    def agregarAparato(self, unAparato):
        if isinstance(unAparato, Aparato):
            nodo = Nodo(unAparato)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo=nodo
            self.__actual=nodo
            self.__tope+=1

    def __str__(self):
        s = ''
        for aparato in self:
            s += str(aparato)+'\n'
        return s    

    def agregarElemento(self, unAparato):
        if isinstance(unAparato, Aparato):
            nodo = Nodo(unAparato)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
            self.__tope += 1
            self.__actual = nodo
            print('Elemento agregado al final de la lista!')

    def insertarElemento(self, posicion, unAparato):
        if isinstance(unAparato, Aparato):
            aux = self.__comienzo
            i = 0
            encontro = False
            ant = aux
            if posicion > 0 and posicion <= self.__tope:
                if i == posicion-1:
                    if aux == None:
                        self.agregarElemento(unAparato)
                    else:
                        nodo=Nodo(unAparato)
                        nodo.setSiguiente(aux)
                        aux.setSiguiente(aux.getSiguiente())
                        self.__comienzo=nodo
                        self.__actual=nodo
                        self.__tope+=1
                else:
                    while aux != None and not encontro:
                        if i == posicion-1:
                            encontro = True
                            nodo = Nodo(unAparato)
                            ant.setSiguiente(nodo)
                            nodo.setSiguiente(aux) 
                            self.__tope+=1
                            print('Elemento agregado en la posicion {}!' .format(posicion))
                        else:
                            ant = aux
                            aux = aux.getSiguiente()
                            i+=1
            else:
                print('ERROR: posicion ingresada invalida!')                         


    def mostrarElemento(self, posicion):
        aux = self.__comienzo
        i = 0
        encontro = False
        if posicion>0 and posicion <= self.__tope:
            if i == posicion-1:
                if isinstance(aux.getDato(), Televisor):
                    print('El tipo de aparato en la posicion {} es televisor' .format(posicion))
                elif isinstance(aux.getDato(), Heladera):
                    print('El tipo de aparato en la posicion {} es heladera' .format(posicion))
                elif isinstance(aux.getDato(), Lavaropa):
                    print('El tipo de aparato en la posicion {} es Lavaropa' .format(posicion))
            else:
                while aux != None and not encontro:
                    if i == posicion-1:
                        encontro = True
                        if isinstance(aux.getDato(), Televisor):
                            print('El tipo de aparato en la posicion {} es televisor' .format(posicion))
                        elif isinstance(aux.getDato(), Heladera):
                            print('El tipo de aparato en la posicion {} es heladera' .format(posicion))
                        elif isinstance(aux.getDato(), Lavaropa):
                            print('El tipo de aparato en la posicion {} es Lavaropa' .format(posicion)) 
                    else:
                        aux = aux.getSiguiente()
                        i+=1
        else:
            print('ERROR: posicion ingresada incorrecta!')        

    def contarPhilips(self):
        aux = self.__comienzo
        count = 0
        encontro = False
        if aux.getDato().getMarca() == 'Philips':
            count+=1
            encontro = True
        else:
            while aux != None:
                if aux.getDato().getMarca() == 'Philips':
                    count+=1
                    encontro = True
                    aux = aux.getSiguiente()
                else:
                    aux = aux.getSiguiente()
        if not encontro:
            print('No hay aparatos de la marca Philips registrados!')

        return count          

    def mostrarMarcaLavarropaSuperior(self):
        aux = self.__comienzo
        encontro = False
        if isinstance(aux.getDato(), Lavaropa) and aux.getDato().getTipoCarga().lower() == 'Superior'.lower():
            print('Marca del lavarropa con tipo de carga superior: {}' .format(aux.getDato().getMarca()))
            aux = aux.getSiguiente()
            encontro = True
        while aux != None:
            if isinstance(aux.getDato(), Lavaropa) and aux.getDato().getTipoCarga().lower() == 'Superior'.lower():
                print('Marca del lavarropa con tipo de carga superior: {}' .format(aux.getDato().getMarca()))
                aux = aux.getSiguiente()
                encontro = True
            else:
                aux = aux.getSiguiente()
        if not encontro:
            print('No hay lavarropa con carga superior registrados!')

    def mostrarDatos(self):
        print('Lista de aparatos registrados:')
        aux = self.__comienzo
        while aux != None:
            aux.getDato().ImporteVenta()
            print(aux.getDato())
            aux = aux.getSiguiente()
                

     





                        
