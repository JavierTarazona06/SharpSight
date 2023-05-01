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

def ordenar_lista(Lista_Doblemente_Encadenada):
        
        actual1 = Lista_Doblemente_Encadenada.head
        while actual1:
            actual2 = actual1.next
            while actual2:
                if actual1.key > actual2.key:
                    actual1.key, actual2.key = actual2.key, actual1.key
                actual2 = actual2.next
            actual1 = actual1.next


def actualizacion(Lista_Doblemente_Encadenada):

    ordenar_lista(Lista_Doblemente_Encadenada)


##Consulta de todos los datos

def imprimir_lista(Lista_Doblemente_Encadenada):
    actual = Lista_Doblemente_Encadenada.head
    while actual:
        print(actual.key, end=' ')
        actual = actual.next
    print()


def eliminacion(Lista_Doblemente_Encadenada):

    Lista_Doblemente_Encadenada.popBack()


def mejor_dato(Lista_Doblemente_Encadenada):

    actualizacion(Lista_Doblemente_Encadenada)

    return Lista_Doblemente_Encadenada.head



   

insercion(Lista_Doblemente_Encadenada)

actualizacion(Lista_Doblemente_Encadenada)

#Lista_Doblemente_Encadenada.imprimir_lista()

eliminacion(Lista_Doblemente_Encadenada)

imprimir_lista(Lista_Doblemente_Encadenada)





    



   