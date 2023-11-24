def add_data(time_final, n, table):
    '''
    Añade una fila a la tabla con los datos del algoritmo
    '''
    time_string = f"{time_final:.6f}"                       # Convertimos el tiempo a string
    if isinstance(time_final, float):                       # Comprobamos si pasa por el umbral
        time_string += "(*)"                                # Si pasa, añadimos un asterisco
    exponents = [n**2.9, n**3, n**3.1]
    exponents_str = ["n**2.9", "n**3", "n**3.1"]
    table.field_names = ["n", "t(n) (ns)"] + \
        [f"t(n) / ({exponent})" for exponent in exponents_str]
    table.add_row([f"{n}".ljust(15), time_string] + \
                  [f"{(time_final/exponent):.6f}".ljust(15) for exponent in exponents])
