import pandas as pd

def eliminar_nan(df):
    df_clean = df.dropna()
    return df_clean

def rellenar_nan_con_valor(df, valor):
    df_clean = df.fillna(valor)
    return df_clean

def rellenar_nan_con_media(df):
    df_clean = df.fillna(df.mean())
    return df_clean