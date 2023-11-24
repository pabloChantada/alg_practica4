'''
Pablo Chantada Saborido (pablo.chantada@udc.es)
Aldana Smyna Medina Lostaunau (aldana.medina@udc.es)
'''

import numpy as np
from prettytable import PrettyTable
import time

# ----------------------------- TABLAS ----------------------------- #

def add_data(time_final, n, table):
    '''
    Añade una fila a la tabla con los datos del algoritmo
    '''
    time_string = f"{time_final:.6f}"                       # Convertimos el tiempo a string
    if isinstance(time_final, float):                       # Comprobamos si pasa por el umbral
        time_string += "(*)"                                # Si pasa, añadimos un asterisco
    exponents = [n**2.9, n**2.97, n**3.1]                   # Exponentes de las cotas
    exponents_str = ["n**2.9", "n**2.97", "n**3.1"]            # Exponentes de las cotas en string
    # Añadimos los nombres de las columnas
    table.field_names = ["n", "t(n) (ns)"] + \
        [f"t(n) / ({exponent})" for exponent in exponents_str]  
    # Añadimos los datos a la tabla
    table.add_row([f"{n}".ljust(5), time_string.ljust(5)] + \
                  [f"{(time_final/exponent):.6f}".ljust(5) for exponent in exponents])       

def tablas_dijsktra(iterations):
    '''
    Test de complejidad de dijsktra con tamaño de la matriz incial 16
    '''
    n = 16                                          # Tamaño inicial de la matriz
    table = PrettyTable()                           # Contruccion de la tabla del algoritmo
    for _ in range(iterations):                     # Iteramos el algoritmo las veces que se indique
        matriz = matrizAleatoria(n)                 # Generacion de la matriz
        time_start = time.perf_counter_ns()         # Inicio del contador
        dijkstra(matriz)                            # Ejecucion del algoritmo
        time_end = time.perf_counter_ns()           # Fin del contador
        time_final = time_end - time_start          # Calculo del tiempo final
        if time_final < 1000000:                    # Situamos el umbral de confianza en 1.000.000ns
            time_final = umbral(n)                  # Ejecutamos el umbral de confianza
        add_data(time_final, n, table)              # Añadimos la fila a la tabla
        n*=2                                        # Duplicamos el tamaño el tamaño de la matriz
    return table

def umbral(n):
    '''
    Umbral de confianza al no pasar el 1.000.000ns
    '''
    k = 1000                                        # Numero de iteraciones
    time_start = time.perf_counter_ns()             # Inicio del contador 1
    for _ in range(k):
        matriz = matrizAleatoria(n)                 # Generacion de la matriz y ejecucion de matrizAleatoria(n)
        dijkstra(matriz)                            # Ejecucion del algoritmo
    time_end = time.perf_counter_ns()               # Fin del contador 1
    time_final1 = time_end - time_start             # Calculo del tiempo total (algoritmo + generacion de la matriz)

    time_start = time.perf_counter_ns()             # Inicio del contador 2
    for _ in range(k):                              # Generacion de la matriz
        matrizAleatoria(n)                          # Generacion de la matriz
    time_end = time.perf_counter_ns()               # Fin del contador 2
    time_final2 = time_end - time_start             # Calculo del tiempo de generacion de la matriz
    # (tiempo total - tiempo de generacion del vector) / numero de iteraciones
    time_final = (time_final1 - time_final2) / k    # Tiempo medio final
    return time_final

# ----------------------------- MATRICES DE EJEMPLO ----------------------------- #

def matrizAleatoria(n):
    '''
    Genera una matriz aleatoria de tamaño n con valores entre 1 y 1000; y 
    diagonal principal a 0
    '''
    m = np.random.randint(low=1, high=1000, size=(n,n))
    return(np.tril(m, -1) + np.tril(m, -1).T)

matrix1 = [
    [0, 1, 4, 7],
    [1, 0, 2, 8],
    [4, 2, 0, 3],
    [7, 8, 3, 0]
]

matrix2 = [
    [0, 1, 8, 4, 7],
    [1, 0, 2, 6, 5],
    [8, 2, 0, 9, 5],
    [4, 6, 9, 0, 3],
    [7, 5, 5, 3, 0]
]

# ----------------------------- DIJKSTRA ----------------------------- #

def dijkstra(M):
    '''
    Devuelve la matriz de distancias minimas de una matriz de adyacencia
    '''
    num_nodos = len(M)                                              # Numero de nodos
    Distancias = np.array(M)                                        # Matriz de distancias              
    for m in range(num_nodos):                                      # Iteramos sobre los nodos
        noVisitados = list(set(range(num_nodos)) - {m})             # Lista de nodos no visitados
        for i in range(num_nodos):                                  # Iteramos sobre los nodos                    
            Distancias[m][i] = M[m][i]                              # Inicializamos la matriz de distancias
        # Usamos -2 porque el nodo inicial ya esta visitado y el nodo final no tiene nodos adyacentes
        for _ in range(num_nodos - 2):                              # Iteramos sobre los nodos menos 2
            v = min(noVisitados, key=lambda x: Distancias[m][x])    # Nodo con menor distancia
            noVisitados.remove(v)                                   # Eliminamos el nodo de la lista de no visitados
            for w in noVisitados:                                   # Iteramos sobre los nodos no visitados    
                if Distancias[m][w] > Distancias[m][v] + M[v][w]:   # Si la distancia es mayor que la distancia del nodo
                    Distancias[m][w] = Distancias[m][v] + M[v][w]   # con menor distancia + la distancia entre el nodo y el nodo con menor distancia
                                                                    # actualizamos la distancia
    return Distancias   

# ----------------------------- TEST ----------------------------- #

def test_complejidades(tablas, iteraciones):
    '''
    Test de complejidad de dijsktra con matrices de tamaño incial 16
    '''
    for _ in range(tablas):              # Matrices de tamaño 1024 como maximo
        print(tablas_dijsktra(iteraciones))

def print_dijkstra(matriz, tamano):
    '''
    Imprime una matriz de ejemplo
    '''
    print("\nMatriz Adyacencia")
    for i in range(tamano):              # Mostramos la matriz de ejemplo
        print(matriz[i])
    matriz_final = dijkstra(matriz)      # Calculamos la matriz de distancias minimas
    print("\nMatriz Distancias Minimas\n")
    for i in range(tamano):              # Mostramos la matriz de distancias minimas 2
        print(matriz_final[i]) 
    
def test_dijkstra():
    '''
    Test de dijkstra con las matrices de ejemplo
    '''
    print_dijkstra(matrix1, 4)           # Mostramos la matriz1 de ejemplo
    print_dijkstra(matrix2, 5)           # Mostramos la matriz2 de ejemplo
    
if __name__ == "__main__":
    test_dijkstra()
    test_complejidades(4, 7)            # Test de complejidad con 4 tablas y 7 iteraciones (maximo 7 iteraciones)