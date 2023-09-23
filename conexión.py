import pandas as pd
import requests
from sodapy import Socrata

def importar_datos_desde_csv(ruta_csv):   
    return pd.read_csv(ruta_csv)

def importar_datos_desde_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Verificar si la solicitud fue exitosa
    return pd.read_csv(pd.compat.StringIO(response.text))

def importar_datos_desde_socrata(domain, dataset_id, app_token=None, limit=None):
    client = Socrata(domain, app_token)
    results = client.get(dataset_id, limit=limit)
    return pd.DataFrame.from_records(results)