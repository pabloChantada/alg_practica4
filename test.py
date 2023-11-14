import numpy as np
import time
from main import dijkstra
from numpy import random  

def matrizAleaotoria(n):
    m = random.randint(low=0, high=1000, size=(n,n))
    return (np.tril(m - 1) + np.tril(m, -1).T) 

def umbral(n):
    '''
    Umbral de confianza al no pasar el 1.000.000ns
    '''
    k = 1000                                        # Numero de iteraciones
    time_start = time.perf_counter_ns()             # Inicio del contador 1
    for _ in range(k):
        matriz = matrizAleaotoria(n)                              # Generacion del vector y ejecucion del   matrizAleaotoria(n)               # Generacion del vector segun el orden indicado
        dijkstra(matriz)                           # Ejecucion del algoritmo
    time_end = time.perf_counter_ns()               # Fin del contador 1
    time_final1 = time_end - time_start             # Calculo del tiempo total (algoritmo + generacion del vector)

    time_start = time.perf_counter_ns()             # Inicio del contador 2
    for _ in range(k):                              # Generacion del vector
        matrizAleaotoria(n)                        # Generacion del vector segun el orden indicado
    time_end = time.perf_counter_ns()               # Fin del contador 2
    time_final2 = time_end - time_start             # Calculo del tiempo de la generacion del vector
    # (tiempo total - tiempo de generacion del vector) / numero de iteraciones
    time_final = (time_final1 - time_final2) / k    # Tiempo medio final 
    return time_final                               
'''
def umbral_ascendente(algoritmo, n):
    
    #Umbral de confianza al no pasar el 1.000.000ns (caso ascendente)
    
    k = 1000                                        # Numero de iteraciones
    vector = crearVector(n, sort= 'asc')            # Generacion del vector ascendente
    time_start = time.perf_counter_ns()             # Inicio del contador
    for _ in range(k):                              # Ejecucion unicamente del algoritmo ya que tras su ejecucion
        algoritmo(vector)                           # el vector no se modifica, por lo que no es necesario volver a generarlo               
    time_end = time.perf_counter_ns()               # Fin del contador
    time_final = (time_end - time_start) / k        # Calculo del tiempo medio
    return time_final
'''

