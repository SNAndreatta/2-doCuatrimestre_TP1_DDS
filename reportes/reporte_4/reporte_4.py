from core.dataframe import CustomDataFrame
from core.utils import obtener_red_social, limpiar_links
import pandas as pd
import os

def reporte_4():
    # Cargar sedes
    sedes = CustomDataFrame("data_limpia/SEDES.csv").dataframe

    filas = []
    for _, row in sedes.iterrows():
        pais = row["pais_iso_3"]
        nombre = row["pais_castellano"]
        sede = row["sede_id"]
        redes_links = str(row["redes_sociales"]) if pd.notna(row["redes_sociales"]) else ""
        for link in limpiar_links(redes_links):
            filas.append({
                "pais": pais,
                "nombre": nombre,
                "sede_id": sede,
                "tipo_red": obtener_red_social(link),
                "url": link
            })

    reporte_df = pd.DataFrame(filas)

    # Ordenar por país, sede, tipo de red y url
    reporte_df = reporte_df.sort_values(
        by=["pais", "nombre", "sede_id", "tipo_red", "url"],
        ascending=True
    ).reset_index(drop=True)

    reporte_df.to_csv("reportes/reporte_4/reporte_4.csv", index=False)

    print(reporte_df)
