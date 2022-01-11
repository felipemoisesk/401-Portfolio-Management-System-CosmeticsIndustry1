import pandas as pd
import numpy
import glob

lista_arquivos=[]
for arquivo in glob.glob(r'C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\Nova pasta\arquivos\*xlsx'):
    lista_arquivos.append(arquivo)


tabelas=[]
for arquivo in lista_arquivos:
    tabelas.append(pd.read_excel(arquivo, index_col=0))


tabela_final=pd.concat(tabelas)

print(tabela_final.info())


***************************

import os

path = r"C:\Users\Br96568\Downloads\BasePreco_VD_BR"
y = os.listdir(path)
print(y)

for file in y:
    print(file)