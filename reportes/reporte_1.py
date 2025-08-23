from core.dataframe import CustomDataFrame
import math

def reporte_1():
    pbi = CustomDataFrame("data_limpia/PBI.csv").dataframe
    secciones = CustomDataFrame("data_limpia/SECCIONES.csv").dataframe
    sedes = CustomDataFrame("data_limpia/SEDES.csv").dataframe

    # Renombrar columnas relevantes
    pbi = pbi.rename(columns={"Country Name": "pais_castellano", "2023": "pbi_per_capita_2023"})
    sedes = sedes.rename(columns={"pais_iso_3": "Country Code"})

    # Limpiar espacios en nombres de países
    sedes["pais_castellano"] = sedes["pais_castellano"].str.strip()
    pbi["pais_castellano"] = pbi["pais_castellano"].str.strip()

    # Contar secciones por sede
    secciones_por_sede = secciones.groupby("sede_id").size().reset_index(name="cantidad_secciones")

    # Unir sedes con su cantidad de secciones
    sedes_con_secciones = sedes.merge(secciones_por_sede, on="sede_id", how="left").fillna({"cantidad_secciones": 0})

    # Calcular cantidad de sedes y promedio de secciones por país
    resumen = sedes_con_secciones.groupby(["pais_castellano", "Country Code"]).agg(
        cantidad_sedes=("sede_id", "count"),
        promedio_secciones=("cantidad_secciones", "mean")
    ).reset_index()

    # Agregar PBI per cápita (solo países con PBI → inner join)
    resumen = resumen.merge(pbi[["Country Code", "pbi_per_capita_2023"]], on="Country Code", how="inner")

    # Redondear promedio de secciones
    resumen["promedio_secciones"] = resumen["promedio_secciones"].apply(lambda x: round(x, 2) if not math.isnan(x) else 0)

    # Ordenar el reporte
    resumen = resumen.sort_values(by=["cantidad_sedes", "pais_castellano"], ascending=[False, True])

    resumen.to_csv("reportes/reporte_1.csv", index=False)

    print(resumen)
