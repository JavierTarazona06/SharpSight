from DynamicList import *
from StaticList import *
import matplotlib.pyplot as plt
import time


p=DynamicList()

# Función que realiza operaciones básicas
def basic_operations(n):
    
    start_time = time.time()

    
    p.pushFront(0)

    end_time = time.time()

    return end_time - start_time

# Valores de entrada para la función
n_values = [10, 100, 1000,10000]

# Lista vacía para almacenar los tiempos de ejecución
times = []

# Ejecuta la función para cada valor de entrada y mide el tiempo de ejecución
for n in n_values:
    time_taken = basic_operations(n)
    times.append(time_taken)

# Grafica los resultados
plt.plot(n_values, times, '-o')
plt.xlabel('Número de operaciones básicas')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Complejidad del código')
plt.show()
