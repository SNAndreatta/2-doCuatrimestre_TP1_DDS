from core.dataframe import CustomDataFrame

def tipos_de_redes():
    dataframe_reporte_4 = CustomDataFrame("reportes/reporte_4/reporte_4.csv")

    data = dataframe_reporte_4.get_all_unique_values("tipo_red")

    for dato in data:
        print(dato)