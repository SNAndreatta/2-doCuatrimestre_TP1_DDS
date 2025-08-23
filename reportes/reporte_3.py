from core.dataframe import CustomDataFrame
from core.utils import obtener_red_social
import pandas as pd

def reporte_3():
    # Cargar sedes
    sedes = CustomDataFrame("data_limpia/SEDES.csv").dataframe

    # Expandir la columna de redes sociales separando por "//"
    filas = []
    for _, row in sedes.iterrows():
        pais = row["pais_iso_3"]
        nombre = row["pais_castellano"]
        redes_links = str(row["redes_sociales"]) if pd.notna(row["redes_sociales"]) else ""
        for link in [r.strip() for r in redes_links.split("//") if r.strip()]:
            filas.append({
                "pais": pais,
                "nombre": nombre,
                "red": obtener_red_social(link)
            })

    redes_df = pd.DataFrame(filas)

    # Agrupar por país y contar cantidad de redes distintas
    resumen = (
        redes_df.groupby("pais")["red"]
        .nunique()
        .reset_index(name="cantidad_redes_distintas")
    )

    resumen.to_csv("reportes/reporte_3.csv", index=False)
    print(resumen)