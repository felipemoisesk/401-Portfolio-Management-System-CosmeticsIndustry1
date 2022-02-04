import pandas as pd
import os

i = input('Você deseja atualizar algum dataset?\nDigite [S] ou [N]: ').upper()
while i == 'S':
    print('\n[1] Atualizar BP BR\n'
          '[2] Atualizar PM LT\n'
          '[3] Atualizar VG FULL\n'
         )
    x = int(input('Qual dataset você deseja atualizar?\nDigite o número: '))
    if x == 1:
        # PROCESSAMENTO BP BR
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
            print(f"{arquivo} + anterior, {dadoshistoricos.shape}.")
        print('\n>> Finalizado PROCESSAMENTO de BASE DE PREÇOS VD BR <<\n')
        # DATACLEAN
        print('>> Iniciando DATACLEAN de BASE DE PREÇOS VD BR <<\n')
        newarquivo = dadoshistoricos[['FILE_NAME',
                                      'Status',
                                      'Código de Venda',
                                      'Descrição',
                                      'Categoria']]
        newarquivo = newarquivo.rename(columns={'Categoria': 'CATEGORIA',
                                                'Código de Venda': 'COD_VENDA',
                                                'Descrição': 'DESC_VENDA',
                                                'Status': 'STATUS'})
        newarquivo.dropna(subset=["CATEGORIA"], inplace=True)
        newarquivo["ANO_CICLO"] = newarquivo["FILE_NAME"].str[0:6]
        newarquivo["ANO"] = newarquivo["ANO_CICLO"].str[0:4]
        newarquivo["CICLO"] = newarquivo["ANO_CICLO"].str[4:6]
        newarquivo["CICLO"] = newarquivo.CICLO.astype('int64')
        newarquivo["CICLO"] = newarquivo.CICLO.astype(str)
        newarquivo["CANAL"] = 'Venda Direta'
        newarquivo["PAIS"] = 'Brasil'
        newarquivo["VIGENTE"] = 'SIM'
        newarquivo["ID_PAISCICLO"] = newarquivo["PAIS"] + newarquivo["CICLO"]
        newarquivo["COD_VENDA"] = newarquivo["COD_VENDA"].fillna(0)
        newarquivo["COD_VENDA"] = newarquivo.COD_VENDA.astype('int64')
        newarquivo["COD_VENDA"] = newarquivo.COD_VENDA.astype(str)
        newarquivo["ID_CODVENDAPAISANOCICLO"] = newarquivo["COD_VENDA"] + newarquivo["PAIS"] + newarquivo["ANO"] + newarquivo["CICLO"]
        newarquivo["CICLO"] = newarquivo.CICLO.astype('int64')
        newarquivo["ANO"] = newarquivo.ANO.astype('int64')
        newarquivo = newarquivo.drop_duplicates("ID_CODVENDAPAISANOCICLO")
        newarquivo["COD_VENDA"] = newarquivo.COD_VENDA.astype('int64')
        print('\n>> Finalizado DATACLEAN de BASE DE PREÇOS VD BR <<\n')
        newarquivo.to_excel("../data_output/2022CC_basedpreco.xlsx", index=False)
        print(newarquivo.info())
        i = input('\nVocê deseja atualizar algum dataset?\nDigite [S] ou [N]: ').upper()
    elif x == 2:
        # PROCESSAMENTO PLANEJAMENTO MERCADOLOGICO
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
            #dadoshistoricos.to_excel("../data_output/hisag_basepreco.xlsx", index=False)
            print(f"{arquivo} + anterior, {dadoshistoricos.shape}.")
        print('\n>> Finalizado PROCESSAMENTO de PLANEJAMENTO MERCADOLÓGICO AG HI <<\n')
        # DATACLEAN
        print('>> Iniciando DATACLEAN de PLANEJAMENTO MERCADOLÓGICO AG HI <<\n')
        newarquivo = dadoshistoricos[['FILE_NAME',
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
        print('>> Finalizado DATACLEAN de PLANEJAMENTO MERCADOLÓGICO AG HI <<\n')
        newarquivo.to_excel("../data_output/2021MM_planemerca.xlsx", index=False)
        print(newarquivo.info())
        i = input('\nVocê deseja atualizar algum dataset?\nDigite [S] ou [N]: ').upper()
    elif x == 3:
        print('\n>> Iniciando PROCESSAMENTO de PORTFOLIO VIGENTE <<\n')
        ax01 =              pd.read_excel(r"../data_input/Auxiliares/AX01_cambiociclo.xlsx")
        dirbaseprecobr =    pd.read_excel(r"../data_output/2022CC_basedpreco.xlsx")
        dirbaseprecohisp =  pd.read_excel(r"../data_output/2021MM_planemerca.xlsx")
        dfvigente = pd.concat([dirbaseprecobr, dirbaseprecohisp])
        dfvigente = pd.merge(dfvigente, ax01, how='left', on='ID_PAISCICLO')
        dfvigente = dfvigente.rename(columns={'Mês': 'MES'})
        dfvigente = dfvigente[['STATUS',
                               'COD_VENDA',
                               'DESC_VENDA',
                               'CATEGORIA',
                               'ANO_CICLO',
                               'ANO',
                               'CICLO',
                               'CANAL',
                               'PAIS',
                               'VIGENTE',
                               'ID_PAISCICLO',
                               'ID_CODVENDAPAISANOCICLO',
                               'MES'
                               ]]
        dfvigente["COD_VENDA"] = dfvigente.COD_VENDA.astype(str)
        dfvigente["ANO"] = dfvigente.ANO.astype(str)
        dfvigente["MES"] = dfvigente.MES.astype(str)
        dfvigente["ID_ANOMESPAISCOD"] = dfvigente["ANO"] + dfvigente["MES"] + dfvigente["PAIS"] + dfvigente["COD_VENDA"]
        dfvigente["COD_VENDA"] = dfvigente.COD_VENDA.astype('int64')
        dfvigente["ANO"] = dfvigente.ANO.astype('int64')
        dfvigente["MES"] = dfvigente.MES.astype('int64')
        print('\n>> Finalizando PROCESSAMENTO de PORTFOLIO VIGENTE <<\n')
        dfvigente.to_excel("../data_output/2022YD_skuvigente.xlsx", index=False)
        i = input('\nVocê deseja atualizar algum dataset?\nDigite [S] ou [N]: ').upper()
    else:
        print('\nOpção de atualização INVÁLIDA!')
        i = input('\nVocê deseja atualizar algum dataset?\nDigite [S] ou [N]: ').upper()
print('\nFIM')

