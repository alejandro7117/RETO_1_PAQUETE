import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def contar_valores_nulos(dataframe):
    return dataframe.isna().sum().sum()

def contar_valores_nulos_por_columna(dataframe):
    return dataframe.isna().sum()

def contar_valores_nulos_consecutivos_por_columna(dataframe):
    consecutive_counts = {}
    for columna in dataframe.columns:
        consecutive_count = 0
        max_consecutive_count = 0
        for valor in dataframe[columna].isna():
            if valor:
                consecutive_count += 1
                max_consecutive_count = max(max_consecutive_count, consecutive_count)
            else:
                consecutive_count = 0
        consecutive_counts[columna] = max_consecutive_count
    return consecutive_counts

def mapa_calor_valores_nulos(dataframe):
    plt.figure(figsize=(10, 6))
    sns.heatmap(dataframe.isna(), cmap="viridis", cbar=False)
    plt.title("Mapa de Calor de Valores Nulos")
    plt.show()

def diagrama_cajas_por_columna(dataframe):
    plt.figure(figsize=(12, 8))
    sns.boxplot(data=dataframe, orient="v")
    plt.title("Diagrama de Cajas y Bigotes por Columna")
    plt.xticks(rotation=90)
    plt.show()

def cuartiles_por_columna(dataframe):
    return dataframe.describe().loc[['25%', '50%', '75%']]

def mapa_calor_distancia_media_columna(dataframe):
    plt.figure(figsize=(10, 6))
    sns.heatmap(dataframe.apply(lambda x: x - x.mean()), cmap="coolwarm", cbar=False)
    plt.title("Mapa de Calor de Distancia a la Media de la Columna")
    plt.show()

def mapa_calor_rango_de_valores(dataframe, min_val, max_val):
    plt.figure(figsize=(10, 6))
    mask = (dataframe >= min_val) & (dataframe <= max_val)
    sns.heatmap(mask, cmap="coolwarm", cbar=False)
    plt.title(f"Mapa de Calor del Rango de Valores [{min_val}, {max_val}]")
    plt.show()