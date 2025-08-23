import pandas as pd
from typing import Any

class CustomDataFrame():
    def __init__(self, data_frame_path: str):
        self.data_frame_path = data_frame_path
        self.custom = None
    
    @property
    def dataframe(self) -> pd.DataFrame:
        """El objeto dataframe de pandas creado en base a la ruta proporcionada.

        Returns:
            pd.DataFrame: El dataframe
        """
        return pd.read_csv(self.data_frame_path)

    def new_dataframe(self, columns_list: list[str]) -> pd.DataFrame:
        """Crea un nueva dataframe en base a las columnas especificadas del dataframe original.

        Args:
            columns_list (list[str]): Las columnas a utilizar

        Returns:
            pd.DataFrame: El dataframe modificado
        """
        missing = [col for col in columns_list if col not in self.dataframe.columns]
        if missing:
            raise ValueError(f"Las siguientes columnas no existen en el DataFrame: {missing}")
        
        self.custom = self.dataframe[columns_list].copy()

        return self.custom

    def get_columns(self, use_custom: bool = False) -> list[str]:
        """
        Devuelve la lista de columnas disponibles en el DataFrame.

        Args:
            use_custom (bool): Si es True, devuelve las columnas del DataFrame custom.
                            Si es False (default), devuelve las columnas del DataFrame original.

        Returns:
            list[str]: Lista con los nombres de las columnas.
        """
        if use_custom and self.custom is not None:
            return self.custom.columns.tolist()
        return self.dataframe.columns.tolist()

    def get_column(self, column_name: Any) -> pd.Series:
        "Returns a Series (a one dimensional array) based on a column name"
        column_name = str(column_name)
        return self.dataframe[column_name]

    def get_empty_column(self, column_name: Any, primary_key: str) -> pd.Series:
        column_name = str(column_name)
        primary_key = str(primary_key)
        return pd.Series(self.dataframe.loc[self.dataframe[column_name].isna(), primary_key])

    def get_all_empty_columns(self, primary_key: str) -> list:
        """
        Devuelve una lista de registros con celdas vacías.
        Cada registro contiene: nombre de la columna vacía, valor de la clave primaria, y el índice (número de fila) en el DataFrame.
        """
        primary_key = str(primary_key)

        empty_cells = []

        for column in self.dataframe.columns:
            if self.dataframe[column].isna().sum() > 0:
                missing_rows = self.dataframe[self.dataframe[column].isna()]
                for idx, row in missing_rows.iterrows():
                    empty_cells.append({
                        'columna_vacia': column,
                        'clave_primaria': row[primary_key],
                        'numero_registro': idx + 1
                    })

        return empty_cells

    def get_all_unique_values(self, column: str) -> list:
        """
        Devuelve todos los valores únicos de una columna como lista.
        """
        return self.dataframe[column].dropna().unique().tolist()
    
    def export_custom_to_csv(self, output_path: str, index: bool = False) -> None:
        """
        Exporta el DataFrame custom a un archivo CSV.

        Args:
            output_path (str): Ruta donde guardar el archivo CSV.
            index (bool): Si se guarda o no el índice. Default: False.
        """
        if self.custom is None:
            raise ValueError("El DataFrame custom no ha sido creado. Use 'new_dataframe' primero.")
        
        self.custom.to_csv(output_path, index=index)