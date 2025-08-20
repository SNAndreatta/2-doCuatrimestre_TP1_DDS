
import pandas as pd
from core.dataframe import CustomDataFrame

PBI_CSV="data/PBI_MUNDIAL.csv"

data_frame_pbi = CustomDataFrame(PBI_CSV)

print(data_frame_pbi.get_empty_column(2023, "Country Name"))