import numpy as np
from numpy import random
from prettytable import PrettyTable
import time 
from tabla import add_data

'''
Pablo Chantada Saborido (pablo.chantada@udc.es)
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
'''
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

def matrizAleatoria(n):
    m = random.randint(low=1, high=1000, size=(n,n))
    return(np.tril(m, -1) + np.tril(m, -1).T)

matrix = [
    [0, 1, 4, 7],
    [1, 0, 2, 8],
    [4, 2, 0, 3],
    [7, 8, 3, 0]
]

matrix2 = [
    [0, 1, 3, 4, 6],
    [1, 0, 2, 5, 5],
    [3, 2, 0, 7, 5],
    [4, 5, 7, 0, 3],
    [6, 5, 5, 3, 0]
]


def dijkstra(M):
    num_nodos = len(M)
    Distancias = np.array(M)
    for m in range(num_nodos):
        noVisitados = list(set(range(num_nodos)) - {m})
        for i in range(num_nodos):
            Distancias[m][i] = M[m][i]
        
        for _ in range(num_nodos - 2):
            v = min(noVisitados, key=lambda x: Distancias[m][x])
            noVisitados.remove(v)
            for w in noVisitados:
                if Distancias[m][w] > Distancias[m][v] + M[v][w]:
                    Distancias[m][w] = Distancias[m][v] + M[v][w]
    return Distancias

def tablas_dijsktra(iterations):
    '''
    Test de complejidad del algoritmo con tamaño del vector inicial 128
    '''
    n = 16                                        # Tamaño inicial del vector
    table = PrettyTable()                           # Contruccion de la tabla del algoritmo
    for _ in range(iterations):                     # Iteramos el algoritmo las veces que se indique
        matriz = matrizAleatoria(n)                # Generacion del vector
        time_start = time.perf_counter_ns()         # Inicio del contador
        dijkstra(matriz)                            # Ejecucion del algoritmo
        time_end = time.perf_counter_ns()           # Fin del contador
        time_final = time_end - time_start          # Calculo del tiempo final
        if time_final < 1000000:                    # Situamos el umbral de confianza en 1.000.000ns
            time_final = umbral(n)                                  # Caso descendente o aleatorio (se modifica el vector)'''
        add_data(time_final, n, table)              # Añadimos la fila a la tabla
        n*=2                                        # Duplicamos el tamaño del vector
    return table

print(tablas_dijsktra(7))
print(tablas_dijsktra(7))
print(tablas_dijsktra(7))
