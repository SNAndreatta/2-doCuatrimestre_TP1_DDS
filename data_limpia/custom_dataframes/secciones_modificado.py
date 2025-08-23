from core.dataframe import CustomDataFrame

def SECCIONES_modificado():
    SECCIONES_CSV = "data/lista-secciones.csv"
    data_frame_secciones = CustomDataFrame(SECCIONES_CSV)

    # Seleccionar solo las columnas relevantes
    columnas_relevantes = [
        'sede_id',
        'tipo_seccion'
    ]
    data_frame_secciones.new_dataframe(columnas_relevantes)

    # Exportar DataFrame limpio
    data_frame_secciones.export_custom_to_csv("data_limpia/SECCIONES.csv")
