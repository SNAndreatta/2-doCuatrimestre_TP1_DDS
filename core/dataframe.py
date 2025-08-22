import pandas as pd
from typing import Any

class CustomDataFrame():

    def __init__(self, data_frame_path: str):
        self.data_frame_path = data_frame_path
    
    def get_column(self, column_name: Any) -> pd.Series:
        "Returns a Series (a one dimensional array) based on a column name"
        column_name = str(column_name)
        df = pd.read_csv(self.data_frame_path)
        return df[column_name]

    def get_empty_column(self, column_name: Any, primary_key: str) -> pd.Series:
        column_name = str(column_name)
        primary_key = str(primary_key)
        df = pd.read_csv(self.data_frame_path)
        return pd.Series(df.loc[df[column_name].isna(), primary_key])

    def get_all_empty_columns(self, primary_key: str) -> list:
        """
        Devuelve una lista de registros con celdas vacías.
        Cada registro contiene: nombre de la columna vacía, valor de la clave primaria, y el índice (número de fila) en el DataFrame.
        """
        primary_key = str(primary_key)
        df = pd.read_csv(self.data_frame_path)

        empty_cells = []

        for column in df.columns:
            if df[column].isna().sum() > 0:
                missing_rows = df[df[column].isna()]
                for idx, row in missing_rows.iterrows():
                    empty_cells.append({
                        'columna_vacia': column,
                        'clave_primaria': row[primary_key],
                        'numero_registro': idx + 1
                    })

        return empty_cells

