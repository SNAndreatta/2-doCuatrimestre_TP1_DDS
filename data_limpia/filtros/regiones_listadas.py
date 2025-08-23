from core.dataframe import CustomDataFrame

def regiones_listadas():
    DATOS_CSV="data/lista-sedes-datos.csv"

    data_frame_pbi = CustomDataFrame(DATOS_CSV)

    column = "region_geografica"

    data = data_frame_pbi.get_all_unique_values(column)

    # columnas_relevantes = [
    #     'Country Code',
    #     '2023'
    # ]

    # Recorremos para ver si alguna columna vacía coincide con las relevantes
    for dato in data:
        print(dato)