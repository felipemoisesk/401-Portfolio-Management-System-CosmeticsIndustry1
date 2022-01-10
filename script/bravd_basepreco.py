import pandas as pd
import shutil
import os

path = r"../data_input/BasePreco_VD_BR"
lista_arquivos = os.listdir(path)
data = []
dados_historicos = pd.DataFrame()
for arquivo in lista_arquivos:
    nome_abas1 = ["Base de Preços BR VF", "Base de Preços Presentes"]
    for aba in nome_abas1:
        tabela = pd.read_excel(f"{path}/{arquivo}", sheet_name=aba, index_col=0, header=1)
        tabela['FILE_NAME'] = os.path.basename(arquivo)
        data.append(tabela)
        dados_historicos = pd.concat([dados_historicos, tabela], axis=0, ignore_index=True)
    dados_historicos.to_excel("bravd_basepreco.xlsx", index=False)
    shutil.move(r"../script/bravd_basepreco.xlsx",
                r"../data_output/bravd_basepreco1.xlsx")
    print(f"Somando {arquivo} ao anterior, o número de linhas e colunas são, respectivamente {dados_historicos.shape}")
