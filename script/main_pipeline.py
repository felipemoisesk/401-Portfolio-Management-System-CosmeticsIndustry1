import pandas as pd
import numpy as np
import shutil

i = input('Você deseja atualizar algum dataset?\nDigite [S] ou [N]: ').upper()

while i == 'S':
    print('[ 1] Atualizar BR NC 19\n'
          '[ 2] Atualizar BR NC 20\n'
          '[ 3] Atualizar BR NC 21\n'
          '[X4] Atualizar BR VD 16\n'
          '[X5] Atualizar BR VD 17\n'
          '[ 6] Atualizar BR VD 18\n'
          '[ 7] Atualizar BR VD 19\n'
          '[ 8] Atualizar BR VD 20\n'
          '[ 9] Atualizar BR VD 21\n'
          '[10] Atualizar HI AG 16\n'
          '[11] Atualizar HI AG 17\n'
          '[12] Atualizar HI AG 18\n'
          '[13] Atualizar HI AG 19\n'
          '[14] Atualizar HI AG 20\n'
          '[15] Atualizar HI AG 21\n')
    x = int(input('Qual dataset você deseja atualizar? \n'))

    if x == 1:
        # ATUALIZAR NOVOS CANAIS 2019
        af_brnc_19_20 = "..\data_input\AF01_brasil_novoscanais_19_20.xlsx"
        # leitura de dataset
        # ds_brnc_19 = pd.read_excel(af_brnc_19_20)
        # criar uma lista de valores faltantes
        missing_values = [' -   ', '  -    ', '-']
        # Lendo a base e passando a lista com os missing values:
        ds_brnc_19 = pd.read_excel("..\data_input\AF01_brasil_novoscanais_19_20.xlsx", na_values=missing_values)
        # renomear colunas
        ds_brnc_19 = ds_brnc_19.rename(columns={'Ano': 'ANO', 'Mês': 'MES', 'Negócio': 'CANAL', 'Cód. Venda': 'COD_VENDA',
                                                ' Desc Material ': 'DESC_VENDA', 'Categoria': 'CATEGORIA_SAP',
                                                'Marca': 'MARCA_SAP', ' RB ': 'RB_MOEDALOCAL', ' Qtd Vendida ': 'QTD_VENDIDA',
                                                ' Qtd Dada ': 'QTD_DADA', ' Qtd Faturada ': 'QTD_FATURADA',
                                                'Cód. Material': 'COD_MATERIAL', 'Subcategoria': 'SUBCATEGORIA',
                                                'Marca Ajustada': 'MARCA_AJUSTADO', 'Categoria Ajustada': 'CATEGORIA_AJUSTADO',
                                                'Subcategoria Ajustada': 'SUBCATEGORIA_AJUSTADO', 'Tribos': 'TRIBO'})
        # excluir colunas
        # ds_brnc_19 = ds_brnc_19.drop(columns=['COD_MATERIAL', 'SUBCATEGORIA', 'MARCA_AJUSTADA', 'CATEGORIA_AJUSTADA',
        #                                      'SUBCATEGORIA_AJUSTADA', 'TRIBO'])
        # filtrar uma coluna (série)
        ds_filtrado = ds_brnc_19['ANO'] == 2019
        ds_brnc_19 = ds_brnc_19[ds_filtrado]
        # descobrir o tipo de cada coluna
        print(ds_brnc_19.dtypes)
        # descobrir número de linhas e colunas
        print(ds_brnc_19.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(ds_brnc_19.isnull().sum())
        ds_brnc_19.to_excel("ds_brnc_19.xlsx", index=False)
        # Enviando o arquivo gerado para uma pasta específica no computador
        shutil.move("..\script\ds_brnc_19.xlsx", "..\data_output\DS01_brnc_19.xlsx")

    elif x == 2:
        # ATUALIZAR NOVOS CANAIS 2020
        af_brnc_19_20 = r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF01_brasil_novoscanais_19_20.xlsx"
        # leitura de dataset
        # ds_brnc_20 = pd.read_excel(af_brnc_19_20)
        # criar uma lista de valores faltantes
        missing_values = [' -   ', '  -    ', '-']
        # Lendo a base e passando a lista com os missing values:
        ds_brnc_20 = pd.read_excel(r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF01_brasil_novoscanais_19_20.xlsx", na_values=missing_values)
        # renomear colunas
        ds_brnc_20 = ds_brnc_20.rename(columns={'Ano': 'ANO', 'Mês': 'MES', 'Negócio': 'CANAL', 'Cód. Venda': 'COD_VENDA',
                                                ' Desc Material ': 'DESC_VENDA', 'Categoria': 'CATEGORIA_SAP',
                                                'Marca': 'MARCA_SAP', ' RB ': 'RB_MOEDALOCAL', ' Qtd Vendida ': 'QTD_VENDIDA',
                                                ' Qtd Dada ': 'QTD_DADA', ' Qtd Faturada ': 'QTD_FATURADA',
                                                'Cód. Material': 'COD_MATERIAL', 'Subcategoria': 'SUBCATEGORIA',
                                                'Marca Ajustada': 'MARCA_AJUSTADO', 'Categoria Ajustada': 'CATEGORIA_AJUSTADO',
                                                'Subcategoria Ajustada': 'SUBCATEGORIA_AJUSTADO', 'Tribos': 'TRIBO'})
        # excluir colunas
        # ds_brnc_20 = ds_brnc_20.drop(columns=['COD_MATERIAL', 'SUBCATEGORIA', 'MARCA_AJUSTADA', 'CATEGORIA_AJUSTADA',
        #                                      'SUBCATEGORIA_AJUSTADA', 'TRIBO'])
        # filtrar uma coluna (série)
        ds_filtrado = ds_brnc_20['ANO'] == 2020
        ds_brnc_20 = ds_brnc_20[ds_filtrado]
        # descobrir o tipo de cada coluna
        print(ds_brnc_20.dtypes)
        # descobrir número de linhas e colunas
        print(ds_brnc_20.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(ds_brnc_20.isnull().sum())
        ds_brnc_20.to_excel("ds_brnc_20.xlsx", index=False)
        # Enviando o arquivo gerado para uma pasta específica no computador
        shutil.move(r'C:\Users\Br96568\PycharmProjects\SistemaGestaoPortfolio\ds_brnc_20.xlsx', r'C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\20_Datasets\DS02_brnc_20.xlsx')

    elif x == 3:
        # ATUALIZAR NOVOS CANAIS 2021
        af_brnc_20_21 = r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF02_brasil_novoscanais_20_21.xlsx"
        # leitura de dataset
        # ds_brnc_21 = pd.read_excel(af_brnc_20_21)
        # criar uma lista de valores faltantes
        missing_values = [' -   ', '  -    ', '-']
        # Lendo a base e passando a lista com os missing values:
        ds_brnc_21 = pd.read_excel(r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF02_brasil_novoscanais_20_21.xlsx", na_values=missing_values)
        # renomear colunas
        ds_brnc_21 = ds_brnc_21.rename(columns={'Ano': 'ANO', 'Mês': 'MES', 'Negócio': 'CANAL', 'Cód. Venda': 'COD_VENDA',
                                                ' Desc Material ': 'DESC_VENDA', 'Categoria': 'CATEGORIA_SAP',
                                                'Marca': 'MARCA_SAP', ' RB ': 'RB_MOEDALOCAL', ' Qtd Vendida ': 'QTD_VENDIDA',
                                                ' Qtd Dada ': 'QTD_DADA', ' Qtd Faturada ': 'QTD_FATURADA',
                                                'Cód. Material': 'COD_MATERIAL', 'Subcategoria': 'SUBCATEGORIA',
                                                'Marca Ajustada': 'MARCA_AJUSTADO', 'Categoria Ajustada': 'CATEGORIA_AJUSTADO',
                                                'Subcategoria Ajustada': 'SUBCATEGORIA_AJUSTADO', 'Tribos': 'TRIBO'})
        # excluir colunas
        # ds_brnc_21 = ds_brnc_21.drop(columns=['COD_MATERIAL', 'SUBCATEGORIA', 'MARCA_AJUSTADA', 'CATEGORIA_AJUSTADA',
        #                                      'SUBCATEGORIA_AJUSTADA', 'TRIBO'])
        # filtrar uma coluna (série)
        ds_filtrado = ds_brnc_21['ANO'] == 2021
        ds_brnc_21 = ds_brnc_21[ds_filtrado]
        # descobrir o tipo de cada coluna
        print(ds_brnc_21.dtypes)
        # descobrir número de linhas e colunas
        print(ds_brnc_21.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(ds_brnc_21.isnull().sum())
        ds_brnc_21.to_excel("ds_brnc_21.xlsx", index=False)
        # Enviando o arquivo gerado para uma pasta específica no computador
        shutil.move(r'C:\Users\Br96568\PycharmProjects\401-Sistema-Gestao-Portfolio\script\ds_brnc_21.xlsx', r'C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\20_Datasets\DS03_brnc_21.xlsx')

    elif x == 4:
        # ATUALIZAR VENDA DIRETA 2016
        af_brvd_16_17 = r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF03_brasil_vendadireta_16_17.xlsx"
        # leitura de dataset
        # ds_brvd_16 = pd.read_excel(af_brvd_16_17)
        # criar uma lista de valores faltantes
        missing_values = [' -   ', '  -    ', '-']
        # Lendo a base e passando a lista com os missing values:
        ds_brvd_16 = pd.read_excel(
            r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF03_brasil_vendadireta_16_17.xlsx",
            na_values=missing_values)
        # filtrar uma coluna (série)
        ds_filtrado = ds_brvd_16['Ano'] == 2016
        ds_brvd_16 = ds_brvd_16[ds_filtrado]
        # renomear colunas
        ds_brvd_16 = ds_brvd_16.rename(columns={'Exercício/período': 'EXERCICIO_PERIODO', 'Material': 'COD_MATERIAL',
                                                'Descr Material': 'DESC_MATERIAL', 'Código de Venda': 'COD_VENDA',
                                                'Descr Cod Venda': 'DESC_VENDA', 'Tipo de Produto (Cla': 'TIPO_PRODUTO',
                                                'Categoria SIPATESP - Atributo': 'CATEGORIA_SIPATESP',
                                                'Subcategoria SIPATES': 'SUBCATEGORIA_SIPATESP', 'Tipo SIPATESP': 'TIPO_SIPATESP',
                                                'Categoria de Marketi': 'CATEGORIA_MARKETING', 'SubCat. Marketing': 'SUBCATEGORIA_MARKETING',
                                                'Linha Mercado / UN': 'LINHA_MERCADO', 'Descr. Linha': 'DESC_LINHA_MERCADO',
                                                'Região Estratégica': 'REGIAO_ESTRATEGICA', 'Atividade': 'ATIVIDADE',
                                                'Tipo de operação': 'TIPO_OPERACAO', '  - Itens para Consumo': 'ITEM_CONSUMO',
                                                '      Qtde. Venda Consumo': 'QTD_VENDA_CONSUMO',
                                                '      Qtde. Dada Consumo': 'QTD_DADA_CONSUMO',
                                                '    Quantidade Vendida': 'QTD_VENDIDA',
                                                '  - Quantidade Dada Linhas': 'QTD_DADA_LINHA',
                                                '      Produtos Linhas': 'PRODUTOS_LINHA',
                                                '      Brindes Linhas': 'BRINDE_LINHA',
                                                '      Amostras Linhas': 'AMOSTRA_LINHA',
                                                '      Outras Fam. Linhas': 'OUTRA_FAMILIA_LINHA',
                                                '  - Quantidade Dada Diversos': 'QTD_DADA_DIVERSO',
                                                '      Produtos Diversos': 'PRODUTO_DIVERSO',
                                                '      Brindes Diversos': 'BRINDE_DIVERSO',
                                                '      Amostras Diversos': 'AMOSTRA_DIVERSO',
                                                '      Outras Fam. Diversos': 'OUTRA_FAMILIA_DIVERSO',
                                                '    Preço Médio - RB/Qtde. Vendida': '(PRECO_MEDIO_RB/QTD_VENDIDA)',
                                                '    Preço Médio - RB/Itens para Consumo': '(PRECO_MEDIO_RB/ITEM_CONSUMO)',
                                                '    Preço Médio - RT/Itens para Consumo': '(PRECO_MEDIO_RT/ITEM_CONSUMO)',
                                                '  - Receita Teórica': 'RECEITA_TEORICA',
                                                '      Margem Teórica (%)': 'MARGEM_TEORICA_%',
                                                '      Desconto Preço (SV)': 'DESCONTO_PRECO_SV',
                                                '      Composto Promocional (SV)': 'COMPOSTO_PROMOCIONAL_SV',
                                                '    Receita Bruta': 'RB_MOEDALOCAL',
                                                '  - % Impostos': 'IMPOSTO_%', '      Impostos': 'IMPOSTO',
                                                '  - Receita Líquida': 'RL_MOEDALOCAL', '      CMV': 'CMV',
                                                '    - CMV Composto Promocional s/ Prod. Diversos': 'CMV_COMPOSTO_PROMOCIONAL_SEM_PRODUTO_DIVERSO',
                                                '        Brindes Linhas': 'BRINDE_LINHA',
                                                '        Produtos Linhas': 'PRODUTO_LINHA',
                                                '        Outras Fam. Promocionais': 'OUTRA_FAMILIA_PROMOCIONAL',
                                                '  - Margem Bruta s/ Prod. Diversos': 'MB_SEM_PRODUTO_DIVERSO',
                                                '      % Margem Bruta': 'MB_MOEDALOCAL',
                                                '    Produtos Diversos Alocado': 'PRODUTO_DIVERSO_ALOCADO',
                                                '  - Margem Bruta c/ Produtos Diversos': 'MB_COM_PRODUTO_DIVERSO',
                                                '    Amostras Linhas': 'AMOSTRA_LINHA', 'Marca ajustado*': 'MARCA_AJUSTADO',
                                                'Categoria ajustado*': 'CATEGORIA_AJUSTADO', 'UG *': 'UNIDADE_GLOBAL',
                                                'Desconto Preço a Custo': 'DESCONTO_PRECO_CUSTO', 'Qtde Vendida': 'QTD_VENDIDA',
                                                'Qtde Dada': 'QTD_DADA', 'Quantidade Faturada': 'QTD_FATURADA', 'Status': 'STATUS',
                                                'Ano': 'ANO', 'Mês*': 'MES'})
        # excluir colunas
        ds_brvd_16 = ds_brvd_16.drop(columns=['      % Margem Bruta c/ Produstos Diversos'])
        # descobrir o tipo de cada coluna
        print(ds_brvd_16.dtypes)
        # descobrir número de linhas e colunas
        print(ds_brvd_16.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(ds_brvd_16.isnull().sum())
        # Exporta para Excel
        ds_brvd_16.to_excel("ds_brvd_16.xlsx", index=False)
        # Enviando o arquivo gerado para uma pasta específica no computador
        shutil.move(r'C:\Users\Br96568\PycharmProjects\SistemaGestaoPortfolio\ds_brvd_16.xlsx',
                    r'C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\20_Datasets\DS04_brvd_16.xlsx')

    elif x == 5:
        # ATUALIZAR VENDA DIRETA 2017
        af_brvd_16_17 = r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF03_brasil_vendadireta_16_17.xlsx"
        # leitura de dataset
        # ds_brvd_17 = pd.read_excel(af_brvd_16_17)
        # criar uma lista de valores faltantes
        missing_values = [' -   ', '  -    ', '-']
        # Lendo a base e passando a lista com os missing values:
        ds_brvd_17 = pd.read_excel(
            r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF03_brasil_vendadireta_16_17.xlsx",
            na_values=missing_values)
        # filtrar uma coluna (série)
        ds_filtrado = ds_brvd_17['Ano'] == 2017
        ds_brvd_17 = ds_brvd_17[ds_filtrado]
        # renomear colunas
        ds_brvd_17 = ds_brvd_17.rename(columns={'Exercício/período': 'EXERCICIO_PERIODO', 'Material': 'COD_MATERIAL',
                                                'Descr Material': 'DESC_MATERIAL', 'Código de Venda': 'COD_VENDA',
                                                'Descr Cod Venda': 'DESC_VENDA', 'Tipo de Produto (Cla': 'TIPO_PRODUTO',
                                                'Categoria SIPATESP - Atributo': 'CATEGORIA_SIPATESP',
                                                'Subcategoria SIPATES': 'SUBCATEGORIA_SIPATESP', 'Tipo SIPATESP': 'TIPO_SIPATESP',
                                                'Categoria de Marketi': 'CATEGORIA_MARKETING', 'SubCat. Marketing': 'SUBCATEGORIA_MARKETING',
                                                'Linha Mercado / UN': 'LINHA_MERCADO', 'Descr. Linha': 'DESC_LINHA_MERCADO',
                                                'Região Estratégica': 'REGIAO_ESTRATEGICA', 'Atividade': 'ATIVIDADE',
                                                'Tipo de operação': 'TIPO_OPERACAO', '  - Itens para Consumo': 'ITEM_CONSUMO',
                                                '      Qtde. Venda Consumo': 'QTD_VENDA_CONSUMO',
                                                '      Qtde. Dada Consumo': 'QTD_DADA_CONSUMO',
                                                '    Quantidade Vendida': 'QTD_VENDIDA',
                                                '  - Quantidade Dada Linhas': 'QTD_DADA_LINHA',
                                                '      Produtos Linhas': 'PRODUTOS_LINHA',
                                                '      Brindes Linhas': 'BRINDE_LINHA',
                                                '      Amostras Linhas': 'AMOSTRA_LINHA',
                                                '      Outras Fam. Linhas': 'OUTRA_FAMILIA_LINHA',
                                                '  - Quantidade Dada Diversos': 'QTD_DADA_DIVERSO',
                                                '      Produtos Diversos': 'PRODUTO_DIVERSO',
                                                '      Brindes Diversos': 'BRINDE_DIVERSO',
                                                '      Amostras Diversos': 'AMOSTRA_DIVERSO',
                                                '      Outras Fam. Diversos': 'OUTRA_FAMILIA_DIVERSO',
                                                '    Preço Médio - RB/Qtde. Vendida': '(PRECO_MEDIO_RB/QTD_VENDIDA)',
                                                '    Preço Médio - RB/Itens para Consumo': '(PRECO_MEDIO_RB/ITEM_CONSUMO)',
                                                '    Preço Médio - RT/Itens para Consumo': '(PRECO_MEDIO_RT/ITEM_CONSUMO)',
                                                '  - Receita Teórica': 'RECEITA_TEORICA',
                                                '      Margem Teórica (%)': 'MARGEM_TEORICA_%',
                                                '      Desconto Preço (SV)': 'DESCONTO_PRECO_SV',
                                                '      Composto Promocional (SV)': 'COMPOSTO_PROMOCIONAL_SV',
                                                '    Receita Bruta': 'RB_MOEDALOCAL',
                                                '  - % Impostos': 'IMPOSTO_%', '      Impostos': 'IMPOSTO',
                                                '  - Receita Líquida': 'RL_MOEDALOCAL', '      CMV': 'CMV',
                                                '    - CMV Composto Promocional s/ Prod. Diversos': 'CMV_COMPOSTO_PROMOCIONAL_SEM_PRODUTO_DIVERSO',
                                                '        Brindes Linhas': 'BRINDE_LINHA',
                                                '        Produtos Linhas': 'PRODUTO_LINHA',
                                                '        Outras Fam. Promocionais': 'OUTRA_FAMILIA_PROMOCIONAL',
                                                '  - Margem Bruta s/ Prod. Diversos': 'MB_SEM_PRODUTO_DIVERSO',
                                                '      % Margem Bruta': 'MB_MOEDALOCAL',
                                                '    Produtos Diversos Alocado': 'PRODUTO_DIVERSO_ALOCADO',
                                                '  - Margem Bruta c/ Produtos Diversos': 'MB_COM_PRODUTO_DIVERSO',
                                                '    Amostras Linhas': 'AMOSTRA_LINHA', 'Marca ajustado*': 'MARCA_AJUSTADO',
                                                'Categoria ajustado*': 'CATEGORIA_AJUSTADO', 'UG *': 'UNIDADE_GLOBAL',
                                                'Desconto Preço a Custo': 'DESCONTO_PRECO_CUSTO', 'Qtde Vendida': 'QTD_VENDIDA',
                                                'Qtde Dada': 'QTD_DADA', 'Quantidade Faturada': 'QTD_FATURADA', 'Status': 'STATUS',
                                                'Ano': 'ANO', 'Mês*': 'MES'})
        # excluir colunas
        ds_brvd_17 = ds_brvd_17.drop(columns=['      % Margem Bruta c/ Produstos Diversos'])
        # descobrir o tipo de cada coluna
        print(ds_brvd_17.dtypes)
        # descobrir número de linhas e colunas
        print(ds_brvd_17.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(ds_brvd_17.isnull().sum())
        # Exporta para Excel
        ds_brvd_17.to_excel("ds_brvd_17.xlsx", index=False)
        # Enviando o arquivo gerado para uma pasta específica no computador
        shutil.move(r'C:\Users\Br96568\PycharmProjects\SistemaGestaoPortfolio\ds_brvd_17.xlsx',
                    r'C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\20_Datasets\DS04_brvd_17.xlsx')

    elif x == 6:
        # ATUALIZAR VENDA DIRETA 2018
        af_brvd_18_19 = r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF04_brasil_vendadireta_18_19.xlsx"
        # leitura de dataset
        # ds_brvd_18 = pd.read_excel(af_brvd_18_19)
        # criar uma lista de valores faltantes
        missing_values = [' -   ', '  -    ', '-']
        # Lendo a base e passando a lista com os missing values:
        ds_brvd_18 = pd.read_excel(r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF04_brasil_vendadireta_18_19.xlsx", na_values=missing_values)
        # renomear colunas
        ds_brvd_18 = ds_brvd_18.rename(columns={'MÊS': 'MES', 'CÓD_MATERIAL': 'COD_MATERIAL', 'CÓD_VENDA': 'COD_VENDA',
                                                'RT': 'RT_MOEDALOCAL', 'RB': 'RB_MOEDALOCAL', 'IMPOSTOS': 'IMPOSTO_MOEDALOCAL',
                                                'RL': 'RL_MOEDALOCAL', 'MB': 'MB_MOEDALOCAL', 'QTDE_VENDIDA': 'QTD_VENDIDA',
                                                'QTDE_DADA': 'QTD_DADA', 'QTDE_VENDIDA AJUST': 'QTD_VENDIDA_AJUSTADO',
                                                'QTDE_DADA AJUST': 'QUANTIDADE_DADA_AJUSTADO', 'Quantidade Faturada': 'QTD_FATURADA',
                                                'Marca ajustado': 'MARCA_AJUSTADO', 'Categoria ajustado': 'CATEGORIA_AJUSTADO',
                                                'Subcategoria ajustada': 'SUBCATEGORIA_AJUSTADO', 'UG': 'UNIDADE_GLOBAL',
                                                'Presentes': 'PRESENTE'})
        # excluir colunas
        ds_brvd_18 = ds_brvd_18.drop(columns=['Unnamed: 30'])
        # filtrar uma coluna (série)
        ds_filtrado = ds_brvd_18['ANO'] == 2018
        ds_brvd_18 = ds_brvd_18[ds_filtrado]
        # descobrir o tipo de cada coluna
        print(ds_brvd_18.dtypes)
        # descobrir número de linhas e colunas
        print(ds_brvd_18.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(ds_brvd_18.isnull().sum())
        ds_brvd_18.to_excel("ds_brvd_18.xlsx", index=False)
        # Enviando o arquivo gerado para uma pasta específica no computador
        shutil.move(r'C:\Users\Br96568\PycharmProjects\SistemaGestaoPortfolio\ds_brvd_18.xlsx',
                    r'C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\20_Datasets\DS06_brvd_18.xlsx')

    elif x == 7:
        # ATUALIZAR VENDA DIRETA 2019
        af_brvd_18_19 = r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF04_brasil_vendadireta_18_19.xlsx"
        # leitura de dataset
        # ds_brvd_18 = pd.read_excel(af_brvd_18_19)
        # criar uma lista de valores faltantes
        missing_values = [' -   ', '  -    ', '-']
        # Lendo a base e passando a lista com os missing values:
        ds_brvd_19 = pd.read_excel(r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF04_brasil_vendadireta_18_19.xlsx", na_values=missing_values)
        # renomear colunas
        ds_brvd_19 = ds_brvd_19.rename(columns={'MÊS': 'MES', 'CÓD_MATERIAL': 'COD_MATERIAL', 'CÓD_VENDA': 'COD_VENDA',
                                                'RT': 'RT_MOEDALOCAL', 'RB': 'RB_MOEDALOCAL', 'IMPOSTOS': 'IMPOSTO_MOEDALOCAL',
                                                'RL': 'RL_MOEDALOCAL', 'MB': 'MB_MOEDALOCAL', 'QTDE_VENDIDA': 'QTD_VENDIDA',
                                                'QTDE_DADA': 'QTD_DADA', 'QTDE_VENDIDA AJUST': 'QTD_VENDIDA_AJUSTADO',
                                                'QTDE_DADA AJUST': 'QUANTIDADE_DADA_AJUSTADO', 'Quantidade Faturada': 'QTD_FATURADA',
                                                'Marca ajustado': 'MARCA_AJUSTADO', 'Categoria ajustado': 'CATEGORIA_AJUSTADO',
                                                'Subcategoria ajustada': 'SUBCATEGORIA_AJUSTADO', 'UG': 'UNIDADE_GLOBAL',
                                                'Presentes': 'PRESENTE'})
        # excluir colunas
        ds_brvd_19 = ds_brvd_19.drop(columns=['Unnamed: 30'])
        # filtrar uma coluna (série)
        ds_filtrado_ano = ds_brvd_19['ANO'] == 2019
        ds_brvd_19 = ds_brvd_19[ds_filtrado_ano]
        ds_filtrado_status = ds_brvd_19['STATUS'] == 'Real'
        ds_brvd_19 = ds_brvd_19[ds_filtrado_status]
        # descobrir o tipo de cada coluna
        print(ds_brvd_19.dtypes)
        # descobrir número de linhas e colunas
        print(ds_brvd_19.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(ds_brvd_19.isnull().sum())
        ds_brvd_19.to_excel("ds_brvd_19.xlsx", index=False)
        # Enviando o arquivo gerado para uma pasta específica no computador
        shutil.move(r'C:\Users\Br96568\PycharmProjects\SistemaGestaoPortfolio\ds_brvd_19.xlsx',
                    r'C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\20_Datasets\DS07_brvd_19.xlsx')

    elif x == 8:
        # ATUALIZAR VENDA DIRETA 2020
        af_brvd_20_21 = r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF05_brasil_vendadireta_20_21.xlsx"
        # leitura de dataset
        # ds_brvd_20 = pd.read_excel(af_brvd_20_21)
        # criar uma lista de valores faltantes
        missing_values = [' -   ', '  -    ', '-']
        # Lendo a base e passando a lista com os missing values:
        ds_brvd_20 = pd.read_excel(r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF05_brasil_vendadireta_20_21.xlsx", na_values=missing_values)
        # renomear colunas
        ds_brvd_20 = ds_brvd_20.rename(columns={'MÊS': 'MES', 'CÓD_MATERIAL': 'COD_MATERIAL', 'CÓD_VENDA': 'COD_VENDA',
                                                'RT': 'RT_MOEDALOCAL', 'RB': 'RB_MOEDALOCAL', 'IMPOSTOS': 'IMPOSTO_MOEDALOCAL',
                                                'RL': 'RL_MOEDALOCAL', 'MB': 'MB_MOEDALOCAL', 'QTDE_VENDIDA': 'QTD_VENDIDA',
                                                'QTDE_DADA': 'QTD_DADA', 'QTDE_VENDIDA AJUST': 'QTD_VENDIDA_AJUSTADO',
                                                'QTDE_DADA AJUST': 'QUANTIDADE_DADA_AJUSTADA', 'Quantidade Faturada': 'QTD_FATURADA',
                                                'Marca ajustado': 'MARCA_AJUSTADO', 'Categoria ajustado': 'CATEGORIA_AJUSTADO',
                                                'Subcategoria ajustada': 'SUBCATEGORIA_AJUSTADO', 'Tribos': 'TRIBO',
                                                'UG': 'UNIDADE_GLOBAL', 'Presentes': 'PRESENTE', 'Subcat Sipatesp': 'SUBCATEGORIA_SIPATESP',
                                                'Classif Complement': 'CLASSIFICACAO_COMPLEMENTAR'})
        # excluir colunas
        # ds_brvd_20 = ds_brvd_20.drop(columns=['Unnamed: 30'])
        # filtrar uma coluna (série)
        ds_filtrado = ds_brvd_20['ANO'] == 2020
        ds_brvd_20 = ds_brvd_20[ds_filtrado]
        # descobrir o tipo de cada coluna
        print(ds_brvd_20.dtypes)
        # descobrir número de linhas e colunas
        print(ds_brvd_20.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(ds_brvd_20.isnull().sum())
        ds_brvd_20.to_excel("ds_brvd_20.xlsx", index=False)
        # Enviando o arquivo gerado para uma pasta específica no computador
        shutil.move(r'C:\Users\Br96568\PycharmProjects\SistemaGestaoPortfolio\ds_brvd_20.xlsx',
                    r'C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\20_Datasets\DS08_brvd_20.xlsx')

    elif x == 9:
        # ATUALIZAR VENDA DIRETA 2021
        af_brvd_20_21 = r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF05_brasil_vendadireta_20_21.xlsx"
        # leitura de dataset
        # ds_brvd_21 = pd.read_excel(af_brvd_20_21)
        # criar uma lista de valores faltantes
        missing_values = [' -   ', '  -    ', '-']
        # Lendo a base e passando a lista com os missing values:
        ds_brvd_21 = pd.read_excel(r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF05_brasil_vendadireta_20_21.xlsx", na_values=missing_values)
        # renomear colunas
        ds_brvd_21 = ds_brvd_21.rename(columns={'MÊS': 'MES', 'CÓD_MATERIAL': 'COD_MATERIAL', 'CÓD_VENDA': 'COD_VENDA',
                                                'RT': 'RT_MOEDALOCAL', 'RB': 'RB_MOEDALOCAL', 'IMPOSTOS': 'IMPOSTO_MOEDALOCAL',
                                                'RL': 'RL_MOEDALOCAL', 'MB': 'MB_MOEDALOCAL', 'QTDE_VENDIDA': 'QTD_VENDIDA',
                                                'QTDE_DADA': 'QTD_DADA', 'QTDE_VENDIDA AJUST': 'QTD_VENDIDA_AJUSTADO',
                                                'QTDE_DADA AJUST': 'QUANTIDADE_DADA_AJUSTADA', 'Quantidade Faturada': 'QTD_FATURADA',
                                                'Marca ajustado': 'MARCA_AJUSTADO', 'Categoria ajustado': 'CATEGORIA_AJUSTADO',
                                                'Subcategoria ajustada': 'SUBCATEGORIA_AJUSTADO', 'Tribos': 'TRIBO',
                                                'UG': 'UNIDADE_GLOBAL', 'Presentes': 'PRESENTE', 'Subcat Sipatesp': 'SUBCATEGORIA_SIPATESP',
                                                'Classif Complement': 'CLASSIFICACAO_COMPLEMENTAR'})
        # excluir colunas
        # ds_brvd_21 = ds_brvd_21.drop(columns=['Unnamed: 30'])
        # filtrar uma coluna (série)
        ds_filtrado_ano = ds_brvd_21['ANO'] == 2021
        ds_brvd_21 = ds_brvd_21[ds_filtrado_ano]
        ds_filtrado_status = ds_brvd_21['STATUS'] == 'Real'
        ds_brvd_21 = ds_brvd_21[ds_filtrado_status]
        # descobrir o tipo de cada coluna
        print(ds_brvd_21.dtypes)
        # descobrir número de linhas e colunas
        print(ds_brvd_21.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(ds_brvd_21.isnull().sum())
        ds_brvd_21.to_excel("ds_brvd_21.xlsx", index=False)
        # Enviando o arquivo gerado para uma pasta específica no computador
        shutil.move(r'C:\Users\Br96568\PycharmProjects\401-Sistema-Gestao-Portfolio\script\ds_brnc_21.xlsx',
                    r'C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\20_Datasets\DS09_brvd_21.xlsx')

    elif x == 10:
        # ATUALIZAR LATAM HISPANA 2016
        af_hiag_16 = r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF06_hispana_agrupados_16.xlsx"
        # leitura de dataset
        # ds_hiag_16 = pd.read_excel(af_hiag_16)
        # criar uma lista de valores faltantes
        missing_values = [' -   ', '  -    ', '-']
        # Lendo a base e passando a lista com os missing values:
        ds_hiag_16 = pd.read_excel(r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF06_hispana_agrupados_16.xlsx", na_values=missing_values)
        # renomear colunas
        ds_hiag_16 = ds_hiag_16.rename(columns={'País': 'PAIS', 'Ano': 'ANO', 'Ciclo': 'CICLO', 'Tri': 'TRIMESTRE',
                                                'Categoria': 'CATEGORIA_SAP', 'Marca': 'MARCA_SAP', 'CV': 'COD_VENDA',
                                                'Desc CV': 'DESC_VENDA', 'RB Promo': 'RB_PROMOCIONAL', 'RT': 'RT_MOEDALOCAL',
                                                'Desconto SV': 'DESCONTO_SV', 'RB': 'RB_MOEDALOCAL', 'IMP': 'IMPOSTO', 'RL': 'RL_MOEDALOCAL',
                                                'DESC CMV': 'DESCONTO_CMV_MOEDALOCAL', 'COMP CMV': 'COMPOSTO_CMV_MOEDALOCAL', 'MB': 'MB_MOEDALOCAL',
                                                'Qtde Vendida': 'QTD_VENDIDA', 'Qtde Dada': 'QTD_DADA', 'Qtde Faturada': 'QTD_FATURADA',
                                                'Cambio': 'CAMBIO_PRATICADO', 'RT R$': 'RT_BRL', 'Desconto SV R$': 'DESCONTO_SV_BRL',
                                                'RB R$': 'RB_BRL', 'IMP R$': 'IMPOSTO_BRL', 'RL R$': 'RL_BRL', 'CMV R$': 'CMV_BRL',
                                                'DESC CMV R$': 'DESCONTO_CMV_BRL', 'COMP CMV R$': 'COMPOSTO_CMV_BRL', 'MB R$': 'MB_BRL',
                                                'CMV': 'CMV_MOEDALOCAL'})
        # excluir colunas
        #ds_hiag_16 = ds_hiag_16.drop(columns=['País'])
        # filtrar uma coluna (série)
        ds_filtrado = ds_hiag_16['ANO'] == 2016
        ds_hiag_16 = ds_hiag_16[ds_filtrado]
        # descobrir o tipo de cada coluna
        print(ds_hiag_16.dtypes)
        # descobrir número de linhas e colunas
        print(ds_hiag_16.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(ds_hiag_16.isnull().sum())
        ds_hiag_16.to_excel("ds_hiag_16.xlsx", index=False)
        # Enviando o arquivo gerado para uma pasta específica no computador
        shutil.move(r'C:\Users\Br96568\PycharmProjects\SistemaGestaoPortfolio\ds_hiag_16.xlsx',
                    r'C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\20_Datasets\DS10_hiag_16.xlsx')

    elif x == 11:
        # ATUALIZAR LATAM HISPANA 2017
        af_hiag_17_18 = r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF07_hispana_agrupados_17_18.xlsx"
        # leitura de dataset
        # ds_hiag_17 = pd.read_excel(af_hiag_17_18)
        # criar uma lista de valores faltantes
        missing_values = [' -   ', '  -    ', '-']
        # Lendo a base e passando a lista com os missing values:
        ds_hiag_17 = pd.read_excel(r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF07_hispana_agrupados_17_18.xlsx", na_values=missing_values)
        # renomear colunas
        ds_hiag_17 = ds_hiag_17.rename(columns={'País': 'PAIS', 'Ano': 'ANO', 'Ciclo': 'CICLO', 'Tri': 'TRIMESTRE',
                                                'Categoria': 'CATEGORIA_SAP', 'Marca': 'MARCA_SAP', 'CV': 'COD_VENDA',
                                                'Desc CV': 'DESC_VENDA', 'RB Promo': 'RB_PROMOCIONAL', 'RT': 'RT_MOEDALOCAL',
                                                'Desconto SV': 'DESCONTO_SV_MOEDALOCAL', 'RB': 'RB_MOEDALOCAL', 'IMP': 'IMPOSTO', 'RL': 'RL_MOEDALOCAL',
                                                'DESC CMV': 'DESCONTO_CMV', 'COMP CMV': 'COMPOSTO_CMV_MOEDALOCAL', 'MB': 'MB_MOEDALOCAL',
                                                'Qtde Vendida': 'QTD_VENDIDA', 'Qtde Dada': 'QTD_DADA', 'Qtde Faturada': 'QTD_FATURADA',
                                                'Cambio': 'CAMBIO_PRATICADO', 'RT R$': 'RT_BRL', 'Desconto SV R$': 'DESCONTO_SV_BRL',
                                                'RB R$': 'RB_BRL', 'IMP R$': 'IMPOSTO_BRL', 'RL R$': 'RL_BRL', 'CMV R$': 'CMV_BRL',
                                                'DESC CMV R$': 'DESCONTO_CMV_BRL', 'COMP CMV R$': 'COMPOSTO_CMV_BRL', 'MB R$': 'MB_BRL',
                                                'CMV': 'CMV_MOEDALOCAL'})
        # excluir colunas
        #ds_hiag_17 = ds_hiag_17.drop(columns=['País'])
        # filtrar uma coluna (série)
        ds_filtrado = ds_hiag_17['ANO'] == 2017
        ds_hiag_17 = ds_hiag_17[ds_filtrado]
        # descobrir o tipo de cada coluna
        print(ds_hiag_17.dtypes)
        # descobrir número de linhas e colunas
        print(ds_hiag_17.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(ds_hiag_17.isnull().sum())
        ds_hiag_17.to_excel("ds_hiag_17.xlsx", index=False)
        # Enviando o arquivo gerado para uma pasta específica no computador
        shutil.move(r'C:\Users\Br96568\PycharmProjects\SistemaGestaoPortfolio\ds_hiag_17.xlsx',
                    r'C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\20_Datasets\DS11_hiag_17.xlsx')

    elif x == 12:
        # ATUALIZAR LATAM HISPANA 2018
        af_hiag_17_18 = r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF07_hispana_agrupados_17_18.xlsx"
        # leitura de dataset
        # ds_hiag_18 = pd.read_excel(af_hiag_17_18)
        # criar uma lista de valores faltantes
        missing_values = [' -   ', '  -    ', '-']
        # Lendo a base e passando a lista com os missing values:
        ds_hiag_18 = pd.read_excel(r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF07_hispana_agrupados_17_18.xlsx", na_values=missing_values)
        # renomear colunas
        ds_hiag_18 = ds_hiag_18.rename(columns={'País': 'PAIS', 'Ano': 'ANO', 'Ciclo': 'CICLO', 'Tri': 'TRIMESTRE',
                                                'Categoria': 'CATEGORIA_SAP', 'Marca': 'MARCA_SAP', 'CV': 'COD_VENDA',
                                                'Desc CV': 'DESC_VENDA', 'RB Promo': 'RB_PROMOCIONAL', 'RT': 'RT_MOEDALOCAL',
                                                'Desconto SV': 'DESCONTO_SV_MOEDALOCAL', 'RB': 'RB_MOEDALOCAL', 'IMP': 'IMPOSTO', 'RL': 'RL_MOEDALOCAL',
                                                'DESC CMV': 'DESCONTO_CMV', 'COMP CMV': 'COMPOSTO_CMV_MOEDALOCAL', 'MB': 'MB_MOEDALOCAL',
                                                'Qtde Vendida': 'QTD_VENDIDA', 'Qtde Dada': 'QTD_DADA', 'Qtde Faturada': 'QTD_FATURADA',
                                                'Cambio': 'CAMBIO_PRATICADO', 'RT R$': 'RT_BRL', 'Desconto SV R$': 'DESCONTO_SV_BRL',
                                                'RB R$': 'RB_BRL', 'IMP R$': 'IMPOSTO_BRL', 'RL R$': 'RL_BRL', 'CMV R$': 'CMV_BRL',
                                                'DESC CMV R$': 'DESCONTO_CMV_BRL', 'COMP CMV R$': 'COMPOSTO_CMV_BRL', 'MB R$': 'MB_BRL',
                                                'CMV': 'CMV_MOEDALOCAL'})
        # excluir colunas
        #ds_hiag_18 = ds_hiag_18.drop(columns=['País'])
        # filtrar uma coluna (série)
        ds_filtrado = ds_hiag_18['ANO'] == 2018
        ds_hiag_18 = ds_hiag_18[ds_filtrado]
        # descobrir o tipo de cada coluna
        print(ds_hiag_18.dtypes)
        # descobrir número de linhas e colunas
        print(ds_hiag_18.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(ds_hiag_18.isnull().sum())
        ds_hiag_18.to_excel("ds_hiag_18.xlsx", index=False)
        # Enviando o arquivo gerado para uma pasta específica no computador
        shutil.move(r'C:\Users\Br96568\PycharmProjects\SistemaGestaoPortfolio\ds_hiag_18.xlsx',
                    r'C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\20_Datasets\DS12_hiag_18.xlsx')

    elif x == 13:
        # ATUALIZAR LATAM HISPANA 2019
        af_hiag_19_20 = r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF08_hispana_agrupados_19_20.xlsx"
        # leitura de dataset
        # ds_hiag_19 = pd.read_excel(af_hiag_19_20)
        # criar uma lista de valores faltantes
        missing_values = [' -   ', '  -    ', '-']
        # Lendo a base e passando a lista com os missing values:
        ds_hiag_19 = pd.read_excel(r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF08_hispana_agrupados_19_20.xlsx", na_values=missing_values)
        # renomear colunas
        ds_hiag_19 = ds_hiag_19.rename(columns={'Status': 'STATUS', 'País': 'PAIS', 'Ano': 'ANO', 'Ciclo': 'CICLO', 'CV': 'COD_VENDA',
                                                'Descr. CV': 'DESC_VENDA', 'Categoria': 'CATEGORIA_SAP', 'Marca': 'MARCA_SAP',
                                                'RB Promo': 'RB_PROMOCIONAL', 'RT R$': 'RT_BRL', 'Desc SV R$': 'DESCONTO_SV_BRL',
                                                'RB R$': 'RB_BRL', 'Imp R$': 'IMPOSTO_BRL', 'RL R$': 'RL_BRL', 'CMV Total R$': 'CMV_TOTAL_BRL',
                                                'Desc CMV R$': 'DESCONTO_CMV_BRL', 'Comp CMV R$': 'COMPOSTO_CMV_BRL', 'MB R$': 'MB_BRL',
                                                'Câmbio': 'CAMBIO_PRATICADO', 'RT ML': 'RT_MOEDALOCAL', 'Desc SV ML': 'DESCONTO_SV_MOEDALOCAL',
                                                'RB ML': 'RB_MOEDALOCAL', 'Imp ML': 'IMPOSTO_MOEDALOCAL', 'RL ML': 'RL_MOEDALOCAL',
                                                'CMV Total ML': 'CMV_TOTAL_MOEDALOCAL', 'Desc CMV ML': 'DESCONTO_CMV_MOEDALOCAL',
                                                'Comp CMV ML': 'COMPOSTO_CMV_MOEDALOCAL', 'MB ML': 'MB_MOEDALOCAL',
                                                'Qtde Vendida': 'QTD_VENDIDA', 'Qtde Dada': 'QTD_DADA', 'Qtde Faturada': 'QTD_FATURADA',
                                                'Categoria BR': 'CATEGORIA_AJUSTADO', 'Marca BR': 'MARCA_AJUSTADO', 'Tribo': 'TRIBO',
                                                'Subcategoria BR': 'SUBCATEGORIA_AJUSTADO', 'Tri': 'TRIMESTRE'})
        # excluir colunas
        ds_hiag_19 = ds_hiag_19.drop(columns=['Unnamed: 38', 'Unnamed: 39', 'Unnamed: 40', 'Unnamed: 41'])
        # filtrar uma coluna (série)
        ds_filtrado = ds_hiag_19['ANO'] == 2019
        ds_hiag_19 = ds_hiag_19[ds_filtrado]
        # descobrir o tipo de cada coluna
        print(ds_hiag_19.dtypes)
        # descobrir número de linhas e colunas
        print(ds_hiag_19.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(ds_hiag_19.isnull().sum())
        ds_hiag_19.to_excel("ds_hiag_19.xlsx", index=False)
        # Enviando o arquivo gerado para uma pasta específica no computador
        shutil.move(r'C:\Users\Br96568\PycharmProjects\SistemaGestaoPortfolio\ds_hiag_19.xlsx',
                    r'C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\20_Datasets\DS13_hiag_19.xlsx')

    elif x == 14:
        # ATUALIZAR LATAM HISPANA 2020
        af_hiag_20_21 = r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF09_hispana_agrupados_20_21.xlsx"
        # leitura de dataset
        # ds_hiag_20 = pd.read_excel(af_hiag_20_21)
        # criar uma lista de valores faltantes
        missing_values = [' -   ', '  -    ', '-']
        # Lendo a base e passando a lista com os missing values:
        ds_hiag_20 = pd.read_excel(r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF09_hispana_agrupados_20_21.xlsx", na_values=missing_values)
        # renomear colunas
        ds_hiag_20 = ds_hiag_20.rename(columns={'Status': 'STATUS', 'País': 'PAIS', 'Ano': 'ANO', 'Ciclo': 'CICLO', 'CV': 'COD_VENDA',
                                                'Descr. CV': 'DESC_VENDA', 'Categoria': 'CATEGORIA_SAP', 'Marca': 'MARCA_SAP',
                                                'RB Promo': 'RB_PROMOCIONAL', 'RT R$': 'RT_BRL', 'Desc SV R$': 'DESCONTO_SV_BRL',
                                                'RB R$': 'RB_BRL', 'Imp R$': 'IMPOSTO_BRL', 'RL R$': 'RL_BRL', 'CMV Total R$': 'CMV_TOTAL_BRL',
                                                'Desc CMV R$': 'DESCONTO_CMV_BRL', 'Comp CMV R$': 'COMPOSTO_CMV_BRL', 'MB R$': 'MB_BRL',
                                                'Câmbio': 'CAMBIO_PRATICADO', 'RT ML': 'RT_MOEDALOCAL', 'Desc SV ML': 'DESCONTO_SV_MOEDALOCAL',
                                                'RB ML': 'RB_MOEDALOCAL', 'Imp ML': 'IMPOSTO_MOEDALOCAL', 'RL ML': 'RL_MOEDALOCAL',
                                                'CMV Total ML': 'CMV_TOTAL_MOEDALOCAL', 'Desc CMV ML': 'DESCONTO_CMV_MOEDALOCAL',
                                                'Comp CMV ML': 'COMPOSTO_CMV_MOEDALOCAL', 'MB ML': 'MB_MOEDALOCAL',
                                                'Qtde Vendida': 'QTD_VENDIDA', 'Qtde Dada': 'QTD_DADA', 'Qtde Faturada': 'QTD_FATURADA',
                                                'Categoria BR': 'CATEGORIA_AJUSTADO', 'Marca BR': 'MARCA_AJUSTADO', 'Tribo': 'TRIBO',
                                                'Subcategoria BR': 'SUBCATEGORIA_AJUSTADO', 'Tri': 'TRIMESTRE'})
        # excluir colunas
        #ds_hiag_20 = ds_hiag_20.drop(columns=['País'])
        # filtrar uma coluna (série)
        ds_filtrado = ds_hiag_20['ANO'] == 2020
        ds_hiag_20 = ds_hiag_20[ds_filtrado]
        # descobrir o tipo de cada coluna
        print(ds_hiag_20.dtypes)
        # descobrir número de linhas e colunas
        print(ds_hiag_20.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(ds_hiag_20.isnull().sum())
        ds_hiag_20.to_excel("ds_hiag_20.xlsx", index=False)
        # Enviando o arquivo gerado para uma pasta específica no computador
        shutil.move(r'C:\Users\Br96568\PycharmProjects\SistemaGestaoPortfolio\ds_hiag_20.xlsx',
                    r'C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\20_Datasets\DS14_hiag_20.xlsx')

    elif x == 15:
        # ATUALIZAR LATAM HISPANA 2021
        af_hiag_20_21 = r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF09_hispana_agrupados_20_21.xlsx"
        # leitura de dataset
        # ds_hiag_21 = pd.read_excel(af_hiag_20_21)
        # criar uma lista de valores faltantes
        missing_values = [' -   ', '  -    ', '-']
        # Lendo a base e passando a lista com os missing values:
        ds_hiag_21 = pd.read_excel(r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF09_hispana_agrupados_20_21.xlsx", na_values=missing_values)
        # renomear colunas
        ds_hiag_21 = ds_hiag_21.rename(columns={'Status': 'STATUS', 'País': 'PAIS', 'Ano': 'ANO', 'Ciclo': 'CICLO', 'CV': 'COD_VENDA',
                                                'Descr. CV': 'DESC_VENDA', 'Categoria': 'CATEGORIA_SAP', 'Marca': 'MARCA_SAP',
                                                'RB Promo': 'RB_PROMOCIONAL', 'RT R$': 'RT_BRL', 'Desc SV R$': 'DESCONTO_SV_BRL',
                                                'RB R$': 'RB_BRL', 'Imp R$': 'IMPOSTO_BRL', 'RL R$': 'RL_BRL', 'CMV Total R$': 'CMV_TOTAL_BRL',
                                                'Desc CMV R$': 'DESCONTO_CMV_BRL', 'Comp CMV R$': 'COMPOSTO_CMV_BRL', 'MB R$': 'MB_BRL',
                                                'Câmbio': 'CAMBIO_PRATICADO', 'RT ML': 'RT_MOEDALOCAL', 'Desc SV ML': 'DESCONTO_SV_MOEDALOCAL',
                                                'RB ML': 'RB_MOEDALOCAL', 'Imp ML': 'IMPOSTO_MOEDALOCAL', 'RL ML': 'RL_MOEDALOCAL',
                                                'CMV Total ML': 'CMV_TOTAL_MOEDALOCAL', 'Desc CMV ML': 'DESCONTO_CMV_MOEDALOCAL',
                                                'Comp CMV ML': 'COMPOSTO_CMV_MOEDALOCAL', 'MB ML': 'MB_MOEDALOCAL',
                                                'Qtde Vendida': 'QTD_VENDIDA', 'Qtde Dada': 'QTD_DADA', 'Qtde Faturada': 'QTD_FATURADA',
                                                'Categoria BR': 'CATEGORIA_AJUSTADO', 'Marca BR': 'MARCA_AJUSTADO', 'Tribo': 'TRIBO',
                                                'Subcategoria BR': 'SUBCATEGORIA_AJUSTADO', 'Tri': 'TRIMESTRE'})
        # excluir colunas
        #ds_hiag_21 = ds_hiag_21.drop(columns=['País'])
        # filtrar uma coluna (série)
        ds_filtrado_ano = ds_hiag_21['ANO'] == 2021
        ds_hiag_21 = ds_hiag_21[ds_filtrado_ano]
        ds_filtrado_status = ds_hiag_21['STATUS'] == 'Real'
        ds_hiag_21 = ds_hiag_21[ds_filtrado_status]
        # descobrir o tipo de cada coluna
        print(ds_hiag_21.dtypes)
        # descobrir número de linhas e colunas
        print(ds_hiag_21.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(ds_hiag_21.isnull().sum())
        ds_hiag_21.to_excel("ds_hiag_21.xlsx", index=False)
        # Enviando o arquivo gerado para uma pasta específica no computador
        shutil.move(r'C:\Users\Br96568\PycharmProjects\401-Sistema-Gestao-Portfolio\script\ds_brnc_21.xlsx',
                    r'C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\20_Datasets\DS15_hiag_21.xlsx')

    elif x == 16:
        #w ATUALIZAR HISPANA PLANEJAMENTO MERCADOLÓGICO 2020
        af_hipm_20 = r"C:\Users\Br96568\OneDrive - Natura Cosméticos\Área de Trabalho\mvptres_painel_sellin\01_ArquivosFonte\AF10_hispana_planejmercad_20.xlsx"
        # leitura de dataset
        ds_hipm_20 = pd.read_excel(af_hipm_20)
        # renomear colunas
        ds_hipm_20 = ds_hipm_20.rename(columns={'Status': 'STATUS', 'País': 'ANO', 'Año': 'ANO', 'Número Ciclo': 'CICLO',
                                                'Codigo de Venta Producto': 'COD_VENDA'})
        # excluir colunas
        ds_hipm_20 = ds_hipm_20.drop(columns=['Descripcion de Venta Producto',
       'Tipo Comercial', 'Categoría', 'Marca', 'UN', 'RB Promo',
       'Descripcion Promo', 'Cantidad Vendida', 'Cantidad Regalada',
       'Cantidad Total', 'RT R$', 'Descuento a SV R$', 'RB ML', 'RB R$',
       'RL ML', 'RL R$', 'RB R$ / Activas', 'UPC', 'CMV Total R$',
       'Compuesto Total R$', 'Descuento a CMV R$', 'CMV STD Total R$',
       'CMD STD Total R$', 'Desc a CMV STD R$', 'Activas', 'Margen R$',
       'Margen STD R$', 'Esfuerzo Promocional', 'Llave', 'SKU 1',
       'Descripcion SKU 1', 'SKU 2', 'Descripcion SKU 2', 'SKU 3',
       'Descripcion SKU 3', 'x', 'CATEGORÍA MKT', 'SUB MARCA MKT',
       'Tipo comercial MKT', 'PUBLICO 2', 'Dónde se aplica / Eje',
       'Producto / Familia general 2', 'Formato / Familia particular',
       'BENEFICIO/ACTIVO/CLUSTER', 'OCASIÓN DE USO', 'TARGET 2',
       'FRAGANCIA/ACTIVO', 'OTROS', 'En que Portafolio?', 'Llave Portafolio',
       'Check Categoría', 'Check Marca', 'Q', 'Activas Subciclo', 'Subciclo',
       'x.1', 'x.2', 'x.3', 'x.4'])
        # descobrir o tipo de cada coluna
        #print(af_hipm_20.dtypes)
        #print(af_hipm_20.columns)
        # descobrir número de linhas e colunas
        #print(af_hipm_20.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        #print(af_hipm_20.isnull().sum())


    else:
        print('\nOpção de atualização INVÁLIDA!')

    i = input('\nVocê deseja atualizar algum outro dataset?\nDigite [S] ou [N]: ').upper()
print('\nFIM')