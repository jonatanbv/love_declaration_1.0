from listaElementos import ListaElemento
import xml.etree.ElementTree as ET
from xml.dom import minidom





def leerXML(ruta):
    tree = ET.parse(ruta)
    root = tree.getroot()

    listaElementos = ListaElemento()

    for elemento in root.iter('listaElementos'):
        for el in elemento.findall('elemento'):
            
            numAtom = el.find('numeroAtomico').text
            simbolo = el.find('simbolo').text
            element = el.find('nombre').text

            listaElementos.insertarFinal(numAtom, simbolo, element)

    return listaElementos


listaUno = ListaElemento()

listaUno = leerXML('prueba.xml')
listaUno.mostrar()