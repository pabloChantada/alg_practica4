import numpy as np
import time
from main import dijkstra
from numpy import random  
'''
Pablo Chantada Saborido (pablo.chantada@udc.es)
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
'''
def matrizAleatoria(n):
    m = random.randint(low=1, high=1000, size=(n,n))
    return(np.tril(m, -1) + np.tril(m, -1).T)


def umbral(n):
    '''
    Umbral de confianza al no pasar el 1.000.000ns
    '''
    k = 1000                                        # Numero de iteraciones
    time_start = time.perf_counter_ns()             # Inicio del contador 1
    for _ in range(k):
        matriz = matrizAleatoria(n)                              # Generacion del vector y ejecucion del   matrizAleaotoria(n)               # Generacion del vector segun el orden indicado
        dijkstra(matriz)                           # Ejecucion del algoritmo
    time_end = time.perf_counter_ns()               # Fin del contador 1
    time_final1 = time_end - time_start             # Calculo del tiempo total (algoritmo + generacion del vector)

    time_start = time.perf_counter_ns()             # Inicio del contador 2
    for _ in range(k):                              # Generacion del vector
        matrizAleatoria(n)                        # Generacion del vector segun el orden indicado
    time_end = time.perf_counter_ns()               # Fin del contador 2
    time_final2 = time_end - time_start             # Calculo del tiempo de la generacion del vector
    # (tiempo total - tiempo de generacion del vector) / numero de iteraciones
    time_final = (time_final1 - time_final2) / k    # Tiempo medio final 
    return time_final                             