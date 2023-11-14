import numpy 

def add_data(time_final, n, table, sort = None):
    '''
    Añade una fila a la tabla con los datos del algoritmo
    '''
    time_string = f"{time_final:.6f}"                       # Convertimos el tiempo a string
    if isinstance(time_final, float):                       # Comprobamos si pasa por el umbral
        time_string += "(*)"                                # Si pasa, añadimos un asterisco
    exponents = {
        'asc': [n, n*numpy.log(n), n**1.4],                 # Creamos un diccionario con los
        'desc': [n, n*numpy.log(n), n**1.4],                # exponentes para cada tipo de ordenacion
        'rand': [n, n*numpy.log(n), n**1.4],
        'mont': [n**0.8, n, n**1.2]                         # Tiempo de creacion del monticulo
    }
    exponents_str = {                                       # Diccionario con los exponentes en forma de
        'asc': ["n", "n*numpy.log(n)", "n**1.4"],           # string para poder mostrarlos en la tabla
        'desc': ["n", "n*numpy.log(n)", "n**1.4"],
        'rand': ["n", "n*numpy.log(n)", "n**1.4"],
        'mont': ["n**0.8", "n", "n**1.2"]                   # Tiempo de creacion del monticulo
    }
    exps = exponents.get(sort)                              # Segun la ordenacion que se pase, se usa un exponente u otro
    exps_str = exponents_str.get(sort)                      # Hacemos lo mismo con las cabezeras de la tabla
                                                            # Usamos list comprehension para crear los titulos 
                                                            # y valores de las columnas
    table.field_names = ["n", "t(n) (ns)"] + \
        [f"t(n) / ({exponent})" for exponent in exps_str]   # Añadimos la cabezera a la tabla
    table.add_row([f"{n}", time_string] + \
                  [f"{time_final/(exponent):.6f}" for exponent in exps])  # Añadimos la fila a la tabla
