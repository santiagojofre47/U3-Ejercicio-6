from ClaseLista import Lista
from claseObjectEncoder import ObjectEncoder
from claseMenu import Menu

if __name__ == '__main__':
    lista = Lista()
    objetoEncoder = ObjectEncoder()
    objetoMenu = Menu()
    d = objetoEncoder.leerJSONArchivo('aparatoselectronicos.json')
    lista = objetoEncoder.decodificarDiccionario(d)
    print(type(lista))
    objetoMenu.mostrarMenu(lista, objetoEncoder)


    

    
   