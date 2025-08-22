import pandas as pd
from core.dataframe import CustomDataFrame

def columnas_vacias_lista_sedes():
    SECCIONES_CSV="data/lista-secciones.csv"

    data_frame_lista_secciones = CustomDataFrame(SECCIONES_CSV)

    primary_key = "sede_id"

    data = data_frame_lista_secciones.get_all_empty_columns(primary_key)

    for dato in data:
        print(dato)

    print(data_frame_lista_secciones.get_empty_column(primary_key, "sede_desc_castellano"))