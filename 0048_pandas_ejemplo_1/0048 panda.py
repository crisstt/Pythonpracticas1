import pandas as pd
import pandas as ExcelWriter

base_edr_2021= pd.read_csv("C:/Users/zxxma/Documents/Respaldo pc Cristian, programacion\Python/0048_pandas_ejemplo_1/Base_EdR_2021.csv")
print(base_edr_2021)
base_edr_2021.head()
print(base_edr_2021.head())
base_edr_2021.columns
print(base_edr_2021.columns)
print (pd.unique(base_edr_2021["Modalidad"]))
print (pd.unique(base_edr_2021["Clave"]))




