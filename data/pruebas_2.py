from DynamicList import *
from StaticList import *
from LinkedList import *
from Node import *
import pandas as pd
import matplotlib.pyplot as plt
import time





List_dinamic=DynamicList()



series=pd.read_csv("C:\\Users\\Jeison Diaz\\Documents\\structure\\SharpSight\\productos.csv")


c=series.shape

tama=[10, 100, 1000, 10000,100000]

# función a analizar


def mi_funcion(n):

    suma = 0
    
    for i in range(n):
        
        suma += i

        List_dinamic.pushBack(0)

    return suma

# lista de tamaños de entrada a probar
tamanios = [10, 100, 1000, 10000,100000]

# lista para almacenar los tiempos de ejecución
tiempos = []

# medición del tiempo de ejecución para cada tamaño de entrada
for tam in tamanios:
    start_time = time.time()
    mi_funcion(tam)
    tiempos.append(time.time() - start_time)

# graficar los tiempos de ejecución vs. el tamaño de entrada
plt.plot(tamanios, tiempos)
plt.xlabel('Tamaño de entrada')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.show()







