import pandas as pd
import os

# PROCESSAMENTO
print('\n>> Iniciando PROCESSAMENTO de PLANEJAMENTO MERCADOLÓGICO AG HI <<\n')
dirbaseprecohisp = r"../data_input/BasePreco_AG_HI"

listaarquivos = os.listdir(dirbaseprecohisp)
dadosplanilha = []
dadoshistoricos = pd.DataFrame()
for arquivo in listaarquivos:
    tabela = pd.read_excel(f"{dirbaseprecohisp}/{arquivo}", header=0)
    tabela['FILE_NAME'] = os.path.basename(arquivo)
    dadosplanilha.append(tabela)
    dadoshistoricos = pd.concat([dadoshistoricos, tabela], axis=0, ignore_index=True)
    dadoshistoricos.to_excel("../data_output/hisag_basepreco.xlsx", index=False)
    print(f"{arquivo} + anterior, {dadoshistoricos.shape}.")
print('\n>> Finalizado PROCESSAMENTO de PLANEJAMENTO MERCADOLÓGICO AG HI <<\n')

# DATACLEAN
print('>> Iniciando DATACLEAN de PLANEJAMENTO MERCADOLÓGICO AG HI <<\n')
newdirbaseprecohisp = r"../data_output/hisag_basepreco.xlsx"
newarquivo = pd.read_excel(newdirbaseprecohisp)

newarquivo = newarquivo[['FILE_NAME',
                         'Status',
                         'Codigo de Venta Producto',
                         'Descripcion de Venta Producto',
                         'Categoría',
                         'Ciclo',
                         'País']]
newarquivo = newarquivo.rename(columns={'Categoría': 'CATEGORIA',
                                        'Codigo de Venta Producto': 'COD_VENDA',
                                        'Descripcion de Venta Producto': 'DESC_VENDA',
                                        'Status': 'STATUS',
                                        'Ciclo': 'ANO_CICLO',
                                        'País': 'PAIS'})

filtrostatus = ['Plan']

newarquivo = newarquivo.loc[newarquivo['STATUS'].isin(filtrostatus)]

newarquivo["COD_VENDA"] = newarquivo.COD_VENDA.astype(str)
newarquivo["ANO_CICLO"] = newarquivo.ANO_CICLO.astype(str)
newarquivo["ANO"] = newarquivo["ANO_CICLO"].str[0:4]
newarquivo["CICLO"] = newarquivo["ANO_CICLO"].str[4:6]
newarquivo["CICLO"] = newarquivo.CICLO.astype('int64')
newarquivo["CICLO"] = newarquivo.CICLO.astype(str)
newarquivo["CANAL"] = 'Agrupados'
newarquivo["VIGENTE"] = 'SIM'
newarquivo["ID_PAISCICLO"] = newarquivo["PAIS"] + newarquivo["CICLO"]
newarquivo["ID_CODVENDAPAISANOCICLO"] = newarquivo["COD_VENDA"] + newarquivo["PAIS"] + newarquivo["ANO_CICLO"]

newarquivo["CICLO"] = newarquivo.CICLO.astype('int64')
newarquivo["ANO"] = newarquivo.ANO.astype('int64')
newarquivo = newarquivo.drop_duplicates("ID_CODVENDAPAISANOCICLO")

newarquivo["COD_VENDA"] = newarquivo.COD_VENDA.astype('int64')

print('\n>> Finalizado DATACLEAN de PLANEJAMENTO MERCADOLÓGICO AG HI <<\n')

newarquivo.to_excel("../data_output/hisag_basepreco.xlsx", index=False)

print(newarquivo.info())
