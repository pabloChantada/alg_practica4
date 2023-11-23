import numpy 
import numpy
from prettytable import PrettyTable


def add_data(time_final, n, table):
    '''
    Añade una fila a la tabla con los datos del algoritmo
    '''
    time_string = f"{time_final:.6f}"                       # Convertimos el tiempo a string
    if isinstance(time_final, float):                       # Comprobamos si pasa por el umbral
        time_string += "(*)"                                # Si pasa, añadimos un asterisco
    exponents = [n**1.8, n**2, n**2.2]
    exponents_str = ["n**1.8", "n**2", "n**2.2"]
    table.field_names = ["n", "t(n) (ns)"] + \
        [f"t(n) / ({exponent})" for exponent in exponents_str]
    table.add_row([f"{n}", time_string] + \
                  [f"{time_final/(exponent):.6f}" for exponent in exponents])
