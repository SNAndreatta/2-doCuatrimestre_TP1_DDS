import pandas as pd
from core.dataframe import CustomDataFrame

def columnas_vacias_PBI():
    PBI_CSV="data/PBI_MUNDIAL.csv"

    data_frame_pbi = CustomDataFrame(PBI_CSV)

    primary_key = "Country Name"

    data = data_frame_pbi.get_all_empty_columns(primary_key)

    columnas_relevantes = [
        'Country Code',
        '2023'
    ]

    # Recorremos para ver si alguna columna vacía coincide con las relevantes
    for dato in data:
        if dato['columna_vacia'] in columnas_relevantes:
            print(dato)

    print(data_frame_pbi.get_empty_column(primary_key, "Country Code"))