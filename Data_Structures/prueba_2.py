from DynamicList import *
from StaticList import *
from OrderedList import *
import matplotlib.pyplot as plt
from LinkedList import *
from Node import *
import time

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
        #Crear lista
        for i in range(n):
            lista_Prueba.pushBack(Node(5))
        #Análisis
        start_time = time.time()
        lista_Prueba.popBack()
        end_time = time.time()
        times.append(end_time - start_time)

    return times


def grafica(x,y,arg):
    # Grafica los resultados
    plt.style.use('dark_background')
    
    plt.plot(x, y, '-o',color='red',linewidth=5)
    plt.style.use("seaborn")
    plt.xlabel('Número de operaciones')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Complejidad del código: '+arg)
    plt.show()


# Valores de entrada para la función
n_values = [10, 100, 1000,10000,100000,1000000,10000000]



#grafica(n_values,pushFrontDynamic(n_values),"Push Front Dynamic List")


grafica(n_values,popFrontDynamic(n_values),"Pop Front Dynamic List")


#grafica(n_values,pushBackLinkedList(n_values),"Push Back LinkedList")


#grafica(n_values,popBackLinkedList(n_values),"PopFront DynamicList")





