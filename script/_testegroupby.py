import pandas as pd
import numpy as np

file = r'../data_output/202112_perfinbrno.xlsx'
df = pd.read_excel(file)

print(df.dtypes)
print('*'*30)
print(df.shape)
print('*'*30)
print(df.columns)

df['ANO'] = df.ANO.astype(str)
df['MES'] = df.MES.astype(str)

df = df.groupby(['ANO', 'MES', 'CANAL', 'COD_VENDA', 'COD_MATERIAL', 'DESC_MATERIAL',
       'CATEGORIA_SAP', 'MARCA_SAP']).sum()

print(df.shape)
print('*'*30)
print(df.columns)
df.to_excel("testegroupby.xlsx", merge_cells=False)
