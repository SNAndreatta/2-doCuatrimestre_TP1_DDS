from core.dataframe import CustomDataFrame
import pandas as pd

def PBI_modificado():
    PBI_CSV = "data/PBI_MUNDIAL.csv"
    data_frame_pbi = CustomDataFrame(PBI_CSV)

    # Completar datos faltantes en 2023 usando el último valor válido
    for idx, row in data_frame_pbi.dataframe.iterrows():
        if pd.isna(row["2023"]):
            prev_values = row.loc["1960":"2022"].dropna()
            if not prev_values.empty:
                last_value = prev_values.iloc[-1]
                data_frame_pbi.dataframe.at[idx, "2023"] = last_value

    # Obtener registros aún vacíos en 2023
    datos_vacios = data_frame_pbi.get_all_empty_columns("Country Name")
    columnas_relevantes = ['2023']

    # Mostrar los registros que todavía tienen valor vacío
    for dato in datos_vacios:
        if dato['columna_vacia'] in columnas_relevantes:
            print(dato)

    # Eliminar del DataFrame los registros que siguen vacíos en columnas relevantes
    claves_a_borrar = [dato['clave_primaria'] for dato in datos_vacios if dato['columna_vacia'] in columnas_relevantes]
    data_frame_pbi.dataframe = data_frame_pbi.dataframe[~data_frame_pbi.dataframe['Country Name'].isin(claves_a_borrar)]

    # Seleccionar solo las columnas relevantes
    columnas_relevantes = ['Country Name', 'Country Code', '2023']
    data_frame_pbi.new_dataframe(columnas_relevantes)

    # Exportar DataFrame limpio
    data_frame_pbi.export_custom_to_csv("data_limpia/PBI.csv")
