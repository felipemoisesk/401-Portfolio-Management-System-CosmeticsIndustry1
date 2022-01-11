import pandas as pd

diretoriobasepreco = r"../data_output/bravd_basepreco.xlsx"
newarquivo = pd.read_excel(diretoriobasepreco)

newarquivo = newarquivo[['Categoria', 'Código de Venda', 'Descrição', 'Status', 'FILE_NAME']]
newarquivo = newarquivo.rename(columns={'Categoria': 'CATEGORIA', 'Código de Venda': 'COD_VENDA', 'Descrição': 'DESC_VENDA', 'Status': 'STATUS'})

newarquivo['COD_VENDA'] = newarquivo.COD_VENDA.astype(str)

newarquivo["ANO_CICLO"] = newarquivo["FILE_NAME"].str[0:6]

print(newarquivo.info())
