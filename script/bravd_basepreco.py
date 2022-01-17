import pandas as pd
import shutil
import os

# PROCESSAMENTO
print('\n>> Iniciando PROCESSAMENTO de BASE DE PREÇOS VD BR <<\n')
dirbaseprecobr = r"../data_input/BasePreco_VD_BR"

listaarquivos = os.listdir(dirbaseprecobr)
dadosplanilha = []
dadoshistoricos = pd.DataFrame()
for arquivo in listaarquivos:
    nomeabas = ["Base de Preços BR VF", "Base de Preços Presentes"]
    for aba in nomeabas:
        tabela = pd.read_excel(f"{dirbaseprecobr}/{arquivo}", sheet_name=aba, index_col=0, header=1)
        tabela['FILE_NAME'] = os.path.basename(arquivo)
        dadosplanilha.append(tabela)
        dadoshistoricos = pd.concat([dadoshistoricos, tabela], axis=0, ignore_index=True)
    dadoshistoricos.to_excel("bravd_basepreco.xlsx", index=False)
    print(f"{arquivo} + anterior, {dadoshistoricos.shape}.")
shutil.move(r"../script/bravd_basepreco.xlsx",
            r"../data_output/bravd_basepreco.xlsx")
print('\n>> Finalizado PROCESSAMENTO de BASE DE PREÇOS VD BR <<\n')

# DATACLEAN
print('>> Iniciando DATACLEAN de BASE DE PREÇOS VD BR <<\n')
newdirbaseprecobr = r"../data_output/bravd_basepreco.xlsx"
newarquivo = pd.read_excel(newdirbaseprecobr)

newarquivo = newarquivo[['FILE_NAME',
                         'Status',
                         'Código de Venda',
                         'Descrição',
                         'Categoria']]
newarquivo = newarquivo.rename(columns={'Categoria': 'CATEGORIA',
                                        'Código de Venda': 'COD_VENDA',
                                        'Descrição': 'DESC_VENDA',
                                        'Status': 'STATUS'})

newarquivo["ANO_CICLO"] = newarquivo["FILE_NAME"].str[0:6]
newarquivo["ANO"] = newarquivo["ANO_CICLO"].str[0:4]
newarquivo["CICLO"] = newarquivo["ANO_CICLO"].str[4:6]
newarquivo["CICLO"] = newarquivo.CICLO.astype('int64')
newarquivo["CICLO"] = newarquivo.CICLO.astype(str)
newarquivo["CANAL"] = 'Venda Direta'
newarquivo["PAIS"] = 'Brasil'
newarquivo["VIGENTE"] = 'SIM'
newarquivo["ID_PAISCICLO"] = newarquivo["PAIS"] + newarquivo["CICLO"]

newarquivo["CICLO"] = newarquivo.CICLO.astype('int64')
newarquivo["ANO"] = newarquivo.ANO.astype('int64')

filtrostatus = ['Lançamento', 'Vigente', 'Vigente apenas neste ciclo']

newarquivo = newarquivo.loc[newarquivo['STATUS'].isin(filtrostatus)]

print('\n>> Finalizado DATACLEAN de BASE DE PREÇOS VD BR <<\n')

newarquivo.to_excel("bravd_basepreco.xlsx", index=False)

shutil.move(r"../script/bravd_basepreco.xlsx",
            r"../data_output/bravd_basepreco.xlsx")

print(newarquivo.info())
