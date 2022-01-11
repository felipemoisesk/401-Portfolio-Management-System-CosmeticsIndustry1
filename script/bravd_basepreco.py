import pandas as pd
import shutil
import os

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
    shutil.move(r"../script/bravd_basepreco.xlsx",
                r"../data_output/bravd_basepreco.xlsx")
    print(f"Somando {arquivo} ao anterior, o número de linhas e colunas são, respectivamente, {dadoshistoricos.shape}")

