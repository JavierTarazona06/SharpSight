from DynamicList import *
from StaticList import *
import matplotlib.pyplot as plt
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

def pushBackDynamic(n_values):
    times = []
    for n in n_values:
        lista_Prueba = DynamicList()
        #Crear lista
        for i in range(n):
            lista_Prueba.pushBack(i)
        #Análisis
        start_time = time.time()
        lista_Prueba.pushBack(12)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def grafica(x,y,arg):
    # Grafica los resultados
    plt.plot(x, y, '-o')
    plt.style.use("seaborn")
    plt.xlabel('Número de operaciones')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Complejidad del código: '+arg)
    plt.show()


# Valores de entrada para la función
n_values = [10, 100, 1000,10000,100000,1000000]

print("Hola")

#grafica(n_values,pushFrontDynamic(n_values),"Push Front Dynamic List")
#grafica(n_values,pushBackDynamic(n_values),"Push Back Dynamic List")