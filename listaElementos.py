from elemento import Elemento

class ListaElemento:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertarFinal(self, numAtom, simbolo, elemento):
        elemento = Elemento(numAtom, simbolo, elemento)

        if self.primero is None:
            self.primero = elemento
            self.ultimo = elemento
        else:
            elemento.anterior = self.ultimo
            self.ultimo.siguiente = elemento
            self.ultimo = elemento

    def mostrar(self):
        if self.primero is None:
            print('Lista Vacia')
        else:
            aux = self.primero
            while aux is not None:
                print(f'Numero Atomico: {aux.numAtom} -- Simbolo: {aux.simbolo} -- Elemento: {aux.elemento}')
                aux = aux.siguiente

    def orden(self):
        aux = self.primero
        while aux is not None:
            aux2 = aux.siguiente
            while aux2 is not None:
                if int(aux.numAtom) > int(aux2.numAtom):
                    temp = aux.numAtom
                    aux.numAtom = aux2.numAtom
                    aux2.numAtom = temp

                    temp = aux.simbolo
                    aux.simbolo = aux2.simbolo
                    aux2.simbolo = temp

                    temp = aux.elemento
                    aux.elemento = aux2.elemento
                    aux2.elemento = temp

                aux2 = aux2.siguiente
            aux = aux.siguiente

