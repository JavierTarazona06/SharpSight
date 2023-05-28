from data.DynamicList import *
from data.StaticList import *
from data.OrderedList import *
import matplotlib.pyplot as plt
from data.LinkedList import *
from data.Node import *
import time

from data.DoubleLinkedListTail import DoubleLinkedListTail
from data.LinkedListOrdered import LinkedListOrdered
from data.QueueDLLT import QueueDLLT


def pushFrontDynamic(n_values):
    times = []
    for n in n_values:
        lista_Prueba = DynamicList()
        #Crear Lista
        for i in range(n):
            lista_Prueba.pushBack(i)
        #Análisis
        start_time = time.time()
        lista_Prueba.pushFront(12)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def popFrontDynamic(n_values):
    times = []
    for n in n_values:
        lista_Prueba = DynamicList()
        #Crear Lista
        for i in range(n):
            lista_Prueba.pushBack(i)
        #Análisis
        start_time = time.time()
        lista_Prueba.popFront()
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def sortDynamic(n_values):
    times = []
    for n in n_values:
        print("Go")
        lista_Prueba = DynamicList()
        #Crear Lista
        for i in range(n):
            lista_Prueba.pushBack(i)
        #Análisis
        start_time = time.time()
        lista_Prueba.sort()
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def pushBackLinkedList(n_values):
    times = []
    for n in n_values:
        lista_Prueba =LinkedList()
        #Crear lista
        for i in range(n):
            lista_Prueba.pushBack(Node(5))
        #Análisis
        start_time = time.time()
        lista_Prueba.pushBack(Node(5))
        end_time = time.time()
        times.append(end_time - start_time)

    return times

def popBackLinkedList(n_values):
    times = []
    for n in n_values:
        lista_Prueba =LinkedList()
        print("Go")
        #Crear lista
        for i in range(n):
            lista_Prueba.pushBack(Node(5))
        #Análisis
        start_time = time.time()
        lista_Prueba.popBack()
        end_time = time.time()
        times.append(end_time - start_time)

    return times

def pushFrontLinkedList(n_values):
    times = []
    for n in n_values:
        lista_Prueba =LinkedList()
        print("Go")
        #Crear lista
        for i in range(n):
            lista_Prueba.pushFront(Node(i))
        #Análisis
        start_time = time.time()
        lista_Prueba.pushFront(Node(0))
        end_time = time.time()
        times.append(end_time - start_time)

    return times

def pushBackDoubleLinkedListTail(n_values):
    times = []
    for n in n_values:
        lista_Prueba = DoubleLinkedListTail()
        print("Go")
        #Crear lista
        for i in range(n):
            lista_Prueba.pushFront(Node(i))
        #Análisis
        start_time = time.time()
        lista_Prueba.pushBack(Node(0))
        end_time = time.time()
        times.append(end_time - start_time)

    return times


def pushFrontDoubleLinkedListTail(n_values):
    times = []
    for n in n_values:
        lista_Prueba = DoubleLinkedListTail()
        print("Go")
        #Crear lista
        for i in range(n):
            lista_Prueba.pushFront(Node(i))
        #Análisis
        start_time = time.time()
        lista_Prueba.pushFront(Node(0))
        end_time = time.time()
        times.append(end_time - start_time)

    return times

def enqueueDLLT(n_values):
    times = []
    for n in n_values:
        cola = QueueDLLT()
        print("Go")
        #Crear lista
        for i in range(n):
            cola.enqueue(Node(i))
        #Análisis
        start_time = time.time()
        cola.enqueue(Node(0))
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def dequeueDLLT(n_values):
    times = []
    for n in n_values:
        cola = QueueDLLT()
        print("Go")
        #Crear lista
        for i in range(n):
            cola.enqueue(Node(i))
        #Análisis
        start_time = time.time()
        cola.dequeue()
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def findLinkListOrder(n_values):
    times = []
    for n in n_values:
        lista = LinkedListOrdered()
        print("Go")
        #Crear lista
        for i in range(n):
            lista.insert(Node(i))
        #Análisis
        start_time = time.time()
        lista.find(Node(0))
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def findLinkList(n_values):
    times = []
    for n in n_values:
        lista = LinkedList()
        print("Go")
        #Crear lista
        for i in range(n):
            lista.pushBack(Node(i))
        #Análisis
        start_time = time.time()
        lista.find(Node(n-1))
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def grafica(x,y,arg):
    # Grafica los resultados
    plt.style.use('dark_background')
    
    plt.plot(x, y, '-o',color='red',linewidth=5)
    plt.xlabel('Número de operaciones')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Complejidad del código: '+arg)
    plt.show()


# Valores de entrada para la función
n_values = [10, 100, 1000,10000,100000]



#grafica(n_values,pushFrontDynamic(n_values),"Push Front Dynamic List")

#grafica(n_values,popFrontDynamic(n_values),"Pop Front Dynamic List")

#grafica(n_values,sortDynamic(n_values),"Sort Dynamic List")


#grafica(n_values,pushBackLinkedList(n_values),"Push Back LinkedList")

#grafica(n_values,popBackLinkedList(n_values),"PopBack LinkedList")

#grafica(n_values,pushFrontLinkedList(n_values),"PushFront LinkedList")

#grafica(n_values,pushBackDoubleLinkedListTail(n_values),"PushBack DoubleLinkedListTail")

#grafica(n_values,pushFrontDoubleLinkedListTail(n_values),"PushFront DoubleLinkedListTail")

#grafica(n_values,enqueueDLLT(n_values),"Enqueue in Queue using DLLT")

#grafica(n_values,dequeueDLLT(n_values),"Dequeue in Queue using DLLT")

#grafica(n_values,findLinkListOrder(n_values),"Find in linked list in order")

#grafica(n_values,findLinkList(n_values),"Find in linked list")