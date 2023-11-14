import numpy as np
from numpy import random
from test import *
from tabla import add_data
from prettytable import PrettyTable
import time 

def matrizAleaotoria(n):
    m = random.randint(low=0, high=1000, size=(n,n))
    return (np.tril(m - 1) + np.tril(m, -1).T) 

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
    n = len(M)
    Distancias = np.array(M)
    for m in range(n):
        noVisitados = list(set(range(n)) - {m})
        for i in range(n - 1):
            Distancias[m, i] = M[m][i]
        for _ in range(n - 2):
            v = min(noVisitados, key=lambda x: Distancias[m, x])
            noVisitados.remove(v)
            for w in noVisitados:
                if Distancias[m, w] > Distancias[m, v] + M[v][w]:
                    Distancias[m, w] = Distancias[m, v] + M[v][w]
    return Distancias

def test_dijkstra(iterations):
    '''
    Test de complejidad del algoritmo con tamaño del vector inicial 128
    '''
    n = 128                                         # Tamaño inicial del vector
    table = PrettyTable()                           # Contruccion de la tabla del algoritmo
    for _ in range(iterations):                     # Iteramos el algoritmo las veces que se indique
        matriz = matrizAleaotoria(n)                # Generacion del vector
        time_start = time.perf_counter_ns()         # Inicio del contador
        dijkstra(matriz)                            # Ejecucion del algoritmo
        time_end = time.perf_counter_ns()           # Fin del contador
        time_final = time_end - time_start          # Calculo del tiempo final
        if time_final < 1000000:                    # Situamos el umbral de confianza en 1.000.000ns                                  # Caso descendente o aleatorio (se modifica el vector)
            time_final = umbral(n)
        add_data(time_final, n, table)              # Añadimos la fila a la tabla
        n *= 2                                      # Progresion geometrica de 2
    print(table)


print(dijkstra(matrix))
print()
print(dijkstra(matrix2))
print()
test_dijkstra(10)