from LinkedList import *
from Node import *
from DynamicList import *
from StaticList import *
from Stack import *
import pandas as pd
from DoubleLinkedListTail import *


#Procesamiento de datos
lector=pd.read_csv(r'C:\Users\Jeison Diaz\OneDrive\Documentos\GitHub\SharpSight\Data_Structures\productosIphone14.csv')

#for i in range(lector.shape[0]):

    #print(lector['precio'][i])


#Creacion
Lista_Doblemente_Encadenada=DoubleLinkedListTail()


#Insercion Nodo
def insercion(Lista_Doblemente_Encadenada):

    for i in range(lector.shape[0]):

        Lista_Doblemente_Encadenada.pushBack(Node(lector['precio'][i]))


#Actualizacion
def actualizacion(Lista_Doblemente_Encadenada):

    Lista_Doblemente_Encadenada.ordenar_lista()


def eliminacion(Lista_Doblemente_Encadenada):

    Lista_Doblemente_Encadenada.popBack()


def mejor_dato(Lista_Doblemente_Encadenada):

    actualizacion(Lista_Doblemente_Encadenada)

    return Lista_Doblemente_Encadenada.head



   

insercion(Lista_Doblemente_Encadenada)

actualizacion(Lista_Doblemente_Encadenada)

#Lista_Doblemente_Encadenada.imprimir_lista()

eliminacion(Lista_Doblemente_Encadenada)

Lista_Doblemente_Encadenada.imprimir_lista()





    



   