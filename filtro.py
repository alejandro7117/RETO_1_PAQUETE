import pandas as pd

def filtrar_por_columna(dataframe, columna, valor):
    return dataframe[dataframe[columna] == valor]

def filtrar_por_condiciones(dataframe, condiciones):
    for columna, valor in condiciones.items():
        dataframe = dataframe[dataframe[columna] == valor]
    return dataframe

def filtrar_por_condicion_numerica(dataframe, columna, operador, valor):
    if operador == '==':
        return dataframe[dataframe[columna] == valor]
    elif operador == '<':
        return dataframe[dataframe[columna] < valor]
    elif operador == '>':
        return dataframe[dataframe[columna] > valor]
    elif operador == '<=':
        return dataframe[dataframe[columna] <= valor]
    elif operador == '>=':
        return dataframe[dataframe[columna] >= valor]
    else:
        raise ValueError("Operador no válido. Use '==', '<', '>', '<=', o '>='.")
    
def filtrar_por_rango(dataframe, columna, valor_min, valor_max):
    return dataframe[(dataframe[columna] >= valor_min) & (dataframe[columna] <= valor_max)]
