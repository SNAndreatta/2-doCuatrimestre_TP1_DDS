from core.dataframe import CustomDataFrame
import math

def reporte_2():
    pbi = CustomDataFrame("data_limpia/PBI.csv").dataframe
    sedes = CustomDataFrame("data_limpia/SEDES.csv").dataframe

    # Renombrar columnas relevantes
    pbi = pbi.rename(columns={"Country Name": "pais_castellano", "2023": "pbi_per_capita_2023"})
    sedes = sedes.rename(columns={"pais_iso_3": "Country Code"})

    # Limpiar espacios en nombres de países
    sedes["pais_castellano"] = sedes["pais_castellano"].str.strip()
    pbi["pais_castellano"] = pbi["pais_castellano"].str.strip()

    # Eliminar duplicados → una fila por país con sede
    paises_con_sede = sedes.drop_duplicates(subset=["pais_castellano", "Country Code", "region_geografica"])

    # Unir con PBI per cápita (solo países con PBI → inner join)
    paises_con_sede = paises_con_sede.merge(
        pbi[["Country Code", "pbi_per_capita_2023"]],
        on="Country Code",
        how="inner"
    )

    # Agrupar por región
    resumen = paises_con_sede.groupby("region_geografica").agg(
        cantidad_paises=("pais_castellano", "nunique"),
        promedio_pbi_per_capita=("pbi_per_capita_2023", "mean")
    ).reset_index()

    # Redondear promedio PBI
    resumen["promedio_pbi_per_capita"] = resumen["promedio_pbi_per_capita"].apply(
        lambda x: round(x, 2) if not math.isnan(x) else 0
    )

    # Ordenar por promedio de PBI per cápita
    resumen = resumen.sort_values(by="promedio_pbi_per_capita", ascending=False)

    # Guardar CSV
    resumen.to_csv("reportes/reporte_2/reporte_2.csv", index=False)

    print(resumen)
