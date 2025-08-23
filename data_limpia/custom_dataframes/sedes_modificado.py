from core.dataframe import CustomDataFrame

def SEDES_modificado():
    SEDES_CSV = "data/lista-sedes-datos.csv"
    data_frame_sedes = CustomDataFrame(SEDES_CSV)

    # Seleccionar solo las columnas relevantes
    columnas_relevantes = [
        'sede_id', 
        'pais_castellano', 
        'region_geografica',
        'pais_iso_3',
        'estado',
        'redes_sociales'
    ]
    data_frame_sedes.new_dataframe(columnas_relevantes)

    # Exportar DataFrame limpio
    data_frame_sedes.export_custom_to_csv("data_limpia/SEDES.csv")
