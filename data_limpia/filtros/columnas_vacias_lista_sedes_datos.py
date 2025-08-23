from core.dataframe import CustomDataFrame

def columnas_vacias_lista_sedes_datos():
    SEDES_DATOS_CSV = "data/lista-sedes-datos.csv"

    # Inicializamos el dataframe personalizado con el csv de sedes datos
    data_frame_lista_sedes_datos = CustomDataFrame(SEDES_DATOS_CSV)

    primary_key = 'sede_id'

    # Obtenemos todas las columnas vacías por sede (filtradas para las relevantes)
    data = data_frame_lista_sedes_datos.get_all_empty_columns(primary_key)

    # Definimos solo las columnas relevantes según la consigna y estructura del csv
    columnas_relevantes = [
        'sede_id',
        'sede_desc_castellano',
        'pais_iso_3',
        'region_geografica',
        'redes_sociales'
    ]

    # Recorremos para ver si alguna columna vacía coincide con las relevantes
    for dato in data:
        if dato['columna_vacia'] in columnas_relevantes:
            print(dato)

    # Ejemplo: imprimir específicamente qué sedes tienen vacío el campo 'sede_desc_castellano'
    print("Sedes con 'sede_desc_castellano' vacío:")
    print(data_frame_lista_sedes_datos.get_empty_column(primary_key, "sede_desc_castellano"))
