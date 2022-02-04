import pandas as pd

# setup dicionarios e listas
dict_columns = {' Desc Material ': 'DESC_MATERIAL',
                ' Qtd Dada ': 'QTD_DADA',
                ' Qtd Faturada ': 'QTD_FATURADA',
                ' Qtd Vendida ': 'QTD_VENDIDA',
                ' RB ': 'RB_MOEDALOCAL',
                '    Amostras Linhas': '_AMOSTRAS LINHAS',
                '    Preço Médio - RB/Itens para Consumo': '_PREÇO MÉDIO - RB/ITENS PARA CONSUMO',
                '    Preço Médio - RB/Qtde. Vendida': '_PREÇO MÉDIO - RB/QTDE. VENDIDA',
                '    Preço Médio - RT/Itens para Consumo': '_PREÇO MÉDIO - RT/ITENS PARA CONSUMO',
                '    Produtos Diversos Alocado': '_PRODUTOS DIVERSOS ALOCADO',
                '    Quantidade Vendida': '_QUANTIDADE VENDIDA',
                '    Receita Bruta': 'RB',
                '  - % Impostos': '_% IMPOSTOS',
                '  - Itens para Consumo': '_ITENS PARA CONSUMO',
                '  - Margem Bruta c/ Produtos Diversos': '_MARGEM BRUTA C/ PRODUTOS DIVERSOS',
                '  - Margem Bruta s/ Prod. Diversos': '_MARGEM BRUTA S/ PROD. DIVERSOS',
                '  - Quantidade Dada Diversos': '_QUANTIDADE DADA DIVERSOS',
                '  - Quantidade Dada Linhas': '_QUANTIDADE DADA LINHAS',
                '  - Receita Líquida': 'RL',
                '  - Receita Teórica': '_RECEITA TEÓRICA',
                '      % Margem Bruta': '_% MARGEM BRUTA',
                '      % Margem Bruta c/ Produstos Diversos': '_% MARGEM BRUTA C/ PRODUSTOS DIVERSOS',
                '      Amostras Diversos': '_AMOSTRAS DIVERSOS',
                '      Amostras Linhas': '_AMOSTRAS LINHAS',
                '      Brindes Diversos': '_BRINDES DIVERSOS',
                '      Brindes Linhas': '_BRINDES LINHAS',
                '      CMV': 'CMV',
                '      Composto Promocional (SV)': '_COMPOSTO PROMOCIONAL (SV)',
                '      Desconto Preço (SV)': '_DESCONTO PREÇO (SV)',
                '      Impostos': 'IMPOSTOS',
                '      Margem Teórica (%)': '_MARGEM TEÓRICA (%)',
                '      Outras Fam. Diversos': '_OUTRAS FAM. DIVERSOS',
                '      Outras Fam. Linhas': '_OUTRAS FAM. LINHAS',
                '      Produtos Diversos': '_PRODUTOS DIVERSOS',
                '      Produtos Linhas': '_PRODUTOS LINHAS',
                '      Qtde. Dada Consumo': '_QTDE. DADA CONSUMO',
                '      Qtde. Venda Consumo': '_QTDE. VENDA CONSUMO',
                '    - CMV Composto Promocional s/ Prod. Diversos': '_CMV COMPOSTO PROMOCIONAL S/ PROD. DIVERSOS',
                '        Brindes Linhas': '_BRINDES LINHAS',
                '        Outras Fam. Promocionais': '_OUTRAS FAM. PROMOCIONAIS',
                '        Produtos Linhas': '_PRODUTOS LINHAS',
                'Ano': 'ANO',
                'ANO': 'ANO',
                'Atividade': 'ATIVIDADE',
                'Cambio': 'CAMBIO',
                'Câmbio': 'CAMBIO',
                'Categoria': 'CATEGORIA_SAP',
                'Categoria Ajustada': 'CATEGORIA_AJUSTADA',
                'Categoria ajustado': 'CATEGORIA_AJUSTADA',
                'Categoria ajustado*': 'CATEGORIA_AJUSTADA',
                'Categoria BR': 'CATEGORIA_AJUSTADA',
                'Categoria de Marketi': 'CATEGORIA_AJUSTADA',
                'Categoria SIPATESP - Atributo': 'CATEGORIA_SIPATESP',
                'CATEGORIA_MARKETING': 'CATEGORIA_AJUSTADA',
                'Ciclo': 'CICLO',
                'Classif Complement': 'CLASSIF_COMPLEMENT',
                'CMV': 'CMV',
                'CMV R$': 'CMV_BRL',
                'CMV Total ML': 'CMV _TOTAL_MOEDALOCAL',
                'CMV Total R$': 'CMV_TOTAL_BRL',
                'CMV_VENDIDO': 'CMV_VENDIDO',
                'Cód. Material': 'COD_MATERIAL',
                'Cód. Venda': 'COD_VENDA',
                'CÓD_MATERIAL': 'COD_MATERIAL',
                'CÓD_VENDA': 'COD_VENDA',
                'Código de Venda': 'COD_VENDA',
                'COMP CMV': 'COMP_CMV',
                'Comp CMV ML': 'COMP_CMV_MOEDALOCAL',
                'COMP CMV R$': 'COMP_CMV_BRL',
                'Comp CMV R$': 'COMP_CMV_BRL',
                'COMPOSTO_CMV': 'COMP_CMV',
                'COMPOSTO_SV': 'COMP_SV',
                'CV': 'COD_VENDA',
                'DESC CMV': 'DESCONTO_CMV',
                'Desc CMV ML': 'DESCONTO_CMV_MOEDALOCAL',
                'DESC CMV R$': 'DESCONTO_CMV_BRL',
                'Desc CMV R$': 'DESCONTO_CMV_BRL',
                'Desc CV': 'DESC_VENDA',
                'Desc SV ML': 'DESCONTO_SV_MOEDALOCAL',
                'Desc SV R$': 'DESCONTO_SV_BRL',
                'DESC_MATERIAL': 'DESC_MATERIAL',
                'DESC_VENDA': 'DESC_VENDA',
                'Desconto Preço a Custo': 'DESCONTO_PRECO_CUSTO',
                'Desconto SV': 'DESCONTO_SV',
                'Desconto SV R$': 'DESCONTO_SV_BRL',
                'DESCONTO_CMV': 'DESCONTO_CMV',
                'DESCONTO_SV': 'DESCONTO_SV',
                'Descr Cod Venda': 'DESC_VENDA',
                'Descr Material': 'DESC_MATERIAL',
                'Descr. CV': 'DESC_VENDA',
                'Descr. Linha': 'DESC_LINHA',
                'Exercício/período': 'EXERCICIO_PERIODO',
                'IMP': 'IMPOSTOS',
                'Imp ML': 'IMPOSTOS_MOEDALOCAL',
                'IMP R$': 'IMPOSTOS_BRL',
                'Imp R$': 'IMPOSTOS_BRL',
                'IMPOSTOS': 'IMPOSTOS',
                'Linha Mercado / UN': 'LINHA_MERCADO',
                'LINHA_MERCADO': 'LINHA_MERCADO',
                'Marca': 'MARCA_SAP',
                'Marca Ajustada': 'MARCA_AJUSTADA',
                'Marca ajustado': 'MARCA_AJUSTADA',
                'Marca ajustado*': 'MARCA_AJUSTADA',
                'Marca BR': 'MARCA_AJUSTADA',
                'Material': 'DESC_MATERIAL',
                'MB': 'MB',
                'MB ML': 'MB_MOEDALOCAL',
                'MB R$': 'MB_BRL',
                'Mês': 'MES',
                'MÊS': 'MES',
                'Mês*': 'MES',
                'Negócio': 'CANAL',
                'País': 'PAIS',
                'Presentes': 'PRESENTES',
                'Qtde Dada': 'QTD_DADA',
                'Qtde Faturada': 'QTD_FATURADA',
                'Qtde Vendida': 'QTD_VENDIDA',
                'QTDE_DADA': 'QTD_DADA',
                'QTDE_DADA AJUST': 'QTD_DADA_AJUSTADO',
                'QTDE_VENDIDA': 'QTD_VENDIDA_AJUSTADO',
                'QTDE_VENDIDA AJUST': 'QTD_VENDIDA',
                'Quantidade Faturada': 'QTD_FATURADA',
                'RB': 'RB',
                'RB ML': 'RB_MOEDALOCAL',
                'RB Promo': 'RB_PROMO',
                'RB R$': 'RB_BRL',
                'Região Estratégica': 'REGIAO_ESTRATEGICA',
                'RL': 'RL',
                'RL ML': 'RL_MOEDALOCAL',
                'RL R$': 'RL_BRL',
                'RT': 'RT',
                'RT ML': 'RT_MOEDALOCAL',
                'RT R$': 'RT_BRL',
                'STATUS': 'STATUS',
                'Status': 'STATUS',
                'Subcat Sipatesp': 'SUBCATEGORIA_SIPATESP',
                'SubCat. Marketing': 'SUBCATEGORIA_AJUSTADA',
                'Subcategoria': 'SUBCATEGORIA_SAP',
                'Subcategoria Ajustada': 'SUBCATEGORIA_AJUSTADA',
                'Subcategoria ajustada': 'SUBCATEGORIA_AJUSTADA',
                'Subcategoria BR': 'SUBCATEGORIA_AJUSTADA',
                'Subcategoria SIPATES': 'SUBCATEGORIA_SIPATESP',
                'Tipo de operação': 'TIPO_OPERACAO',
                'Tipo de Produto (Cla': 'TIPO_PRODUTO',
                'Tipo SIPATESP': 'TIPO_SIPATESP',
                'TIPO_PRODUTO': 'TIPO_PRODUTO',
                'Tri': 'TRIMESTRE',
                'Tribo': 'TRIBO',
                'Tribos': 'TRIBO',
                'UG': 'UG',
                'UG *': 'UG'
                }
#'País'': 'PAIS',
#'RB Promo'': 'RB_PROMO',
list_missingvalues = [' -   ',
                      '  -    ',
                      '-'
                      ]

i = input('Você deseja atualizar algum dataset?\nDigite [S] ou [N]: ').upper()

while i == 'S':
    print('[ 1] Atualizar BR NC 19\n'
          '[ 2] Atualizar BR NC 20\n'
          '[ 3] Atualizar BR NC 21\n'
          '[ 4] Atualizar BR VD 18\n'
          '[ 5] Atualizar BR VD 19\n'
          '[ 6] Atualizar BR VD 20\n'
          '[ 7] Atualizar BR VD 21\n'
          '[ 8] Atualizar HI AG 18\n'
          '[ 9] Atualizar HI AG 19\n'
          '[10] Atualizar HI AG 20\n'
          '[11] Atualizar HI AG 21\n')
    x = int(input('Qual dataset você deseja atualizar? \n'))
    if x == 1:
        # ATUALIZAR NOVOS CANAIS 2019
        af_brnc_19 = "../data_input/PerformanceFinanceira/AF01_brasil_novoscanais_19_20.xlsx"
        # Lendo a base e passando a lista com os missing values:
        af_brnc_19 = pd.read_excel(af_brnc_19, na_values=list_missingvalues)
        # renomear colunas
        af_brnc_19 = af_brnc_19.rename(columns=dict_columns)
        # filtrar uma coluna (série)
        af_brnc_19 = af_brnc_19[af_brnc_19['ANO'] == 2019]
        # descobrir o tipo de cada coluna
        print(af_brnc_19.dtypes)
        # descobrir número de linhas e colunas
        print(af_brnc_19.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(af_brnc_19.isnull().sum())
        # Enviando o arquivo gerado para uma pasta específica no computador
        af_brnc_19.to_excel("../data_output/DS01_brnc_19.xlsx", index=False)
        i = input('\nVocê deseja atualizar algum outro dataset?\nDigite [S] ou [N]: ').upper()
    elif x == 2:
        # ATUALIZAR NOVOS CANAIS 2020
        af_brnc_20 = "../data_input/PerformanceFinanceira/AF01_brasil_novoscanais_19_20.xlsx"
        # Lendo a base e passando a lista com os missing values:
        af_brnc_20 = pd.read_excel(af_brnc_20, na_values=list_missingvalues)
        # renomear colunas
        af_brnc_20 = af_brnc_20.rename(columns=dict_columns)
        # filtrar uma coluna (série)
        af_brnc_20 = af_brnc_20[af_brnc_20['ANO'] == 2020]
        # descobrir o tipo de cada coluna
        print(af_brnc_20.dtypes)
        # descobrir número de linhas e colunas
        print(af_brnc_20.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(af_brnc_20.isnull().sum())
        # Enviando o arquivo gerado para uma pasta específica no computador
        af_brnc_20.to_excel("../data_output/DS02_brnc_20.xlsx", index=False)
        i = input('\nVocê deseja atualizar algum outro dataset?\nDigite [S] ou [N]: ').upper()
    elif x == 3:
        # ATUALIZAR NOVOS CANAIS 2021
        af_brnc_21 = "../data_input/PerformanceFinanceira/AF02_brasil_novoscanais_20_21.xlsx"
        # Lendo a base e passando a lista com os missing values:
        af_brnc_21 = pd.read_excel(af_brnc_21, na_values=list_missingvalues)
        # renomear colunas
        af_brnc_21 = af_brnc_21.rename(columns=dict_columns)
        # filtrar uma coluna (série)
        af_brnc_21 = af_brnc_21[af_brnc_21['ANO'] == 2021]
        # descobrir o tipo de cada coluna
        print(af_brnc_21.dtypes)
        # descobrir número de linhas e colunas
        print(af_brnc_21.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(af_brnc_21.isnull().sum())
        # Enviando o arquivo gerado para uma pasta específica no computador
        af_brnc_21.to_excel("../data_output/DS03_brnc_21.xlsx", index=False)
        i = input('\nVocê deseja atualizar algum outro dataset?\nDigite [S] ou [N]: ').upper()
    elif x == 4:
        # ATUALIZAR VENDA DIRETA 2018
        af_brvd_18 = "../data_input/PerformanceFinanceira/AF03_brasil_vendadireta_18_19.xlsx"
        # Lendo a base e passando a lista com os missing values:
        af_brvd_18 = pd.read_excel(af_brvd_18, na_values=list_missingvalues)
        # renomear colunas
        af_brvd_18 = af_brvd_18.rename(columns=dict_columns)
        # filtrar uma coluna (série)
        af_brvd_18 = af_brvd_18[af_brvd_18['ANO'] == 2018]
        # descobrir o tipo de cada coluna
        print(af_brvd_18.dtypes)
        # descobrir número de linhas e colunas
        print(af_brvd_18.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(af_brvd_18.isnull().sum())
        # Enviando o arquivo gerado para uma pasta específica no computador
        af_brvd_18.to_excel("../data_output/DS04_brvd_18.xlsx", index=False)
        i = input('\nVocê deseja atualizar algum outro dataset?\nDigite [S] ou [N]: ').upper()
    elif x == 5:
        # ATUALIZAR VENDA DIRETA 2019
        af_brvd_19 = "../data_input/PerformanceFinanceira/AF03_brasil_vendadireta_18_19.xlsx"
        # Lendo a base e passando a lista com os missing values:
        af_brvd_19 = pd.read_excel(af_brvd_19, na_values=list_missingvalues)
        # renomear colunas
        af_brvd_19 = af_brvd_19.rename(columns=dict_columns)
        # filtrar uma coluna (série)
        af_brvd_19 = af_brvd_19[af_brvd_19['ANO'] == 2019]
        # descobrir o tipo de cada coluna
        print(af_brvd_19.dtypes)
        # descobrir número de linhas e colunas
        print(af_brvd_19.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(af_brvd_19.isnull().sum())
        # Enviando o arquivo gerado para uma pasta específica no computador
        af_brvd_19.to_excel("../data_output/DS05_brvd_19.xlsx", index=False)
        i = input('\nVocê deseja atualizar algum outro dataset?\nDigite [S] ou [N]: ').upper()
    elif x == 6:
        # ATUALIZAR VENDA DIRETA 2020
        af_brvd_20 = "../data_input/PerformanceFinanceira/AF04_brasil_vendadireta_20_21.xlsx"
        # Lendo a base e passando a lista com os missing values:
        af_brvd_20 = pd.read_excel(af_brvd_20, na_values=list_missingvalues)
        # renomear colunas
        af_brvd_20 = af_brvd_20.rename(columns=dict_columns)
        # filtrar uma coluna (série)
        af_brvd_20 = af_brvd_20[af_brvd_20['ANO'] == 2020]
        # descobrir o tipo de cada coluna
        print(af_brvd_20.dtypes)
        # descobrir número de linhas e colunas
        print(af_brvd_20.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(af_brvd_20.isnull().sum())
        # Enviando o arquivo gerado para uma pasta específica no computador
        af_brvd_20.to_excel("../data_output/DS06_brvd_20.xlsx", index=False)
        i = input('\nVocê deseja atualizar algum outro dataset?\nDigite [S] ou [N]: ').upper()
    elif x == 7:
        # ATUALIZAR VENDA DIRETA 2021
        af_brvd_21 = "../data_input/PerformanceFinanceira/AF04_brasil_vendadireta_20_21.xlsx"
        # Lendo a base e passando a lista com os missing values:
        af_brvd_21 = pd.read_excel(af_brvd_21, na_values=list_missingvalues)
        # renomear colunas
        af_brvd_21 = af_brvd_21.rename(columns=dict_columns)
        # filtrar uma coluna (série)
        af_brvd_21 = af_brvd_21[af_brvd_21['ANO'] == 2021]
        # descobrir o tipo de cada coluna
        print(af_brvd_21.dtypes)
        # descobrir número de linhas e colunas
        print(af_brvd_21.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(af_brvd_21.isnull().sum())
        # Enviando o arquivo gerado para uma pasta específica no computador
        af_brvd_21.to_excel("../data_output/DS07_brvd_21.xlsx", index=False)
        i = input('\nVocê deseja atualizar algum outro dataset?\nDigite [S] ou [N]: ').upper()
    elif x == 8:
        # ATUALIZAR HISPANA 2018
        af_hiag_18 = "../data_input/PerformanceFinanceira/AF05_hispana_agrupados_17_18.xlsx"
        # Lendo a base e passando a lista com os missing values:
        af_hiag_18 = pd.read_excel(af_hiag_18, na_values=list_missingvalues)
        # renomear colunas
        af_hiag_18 = af_hiag_18.rename(columns=dict_columns)
        # filtrar uma coluna (série)
        af_hiag_18 = af_hiag_18[af_hiag_18['ANO'] == 2018]
        # descobrir o tipo de cada coluna
        print(af_hiag_18.dtypes)
        # descobrir número de linhas e colunas
        print(af_hiag_18.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(af_hiag_18.isnull().sum())
        # Enviando o arquivo gerado para uma pasta específica no computador
        af_hiag_18.to_excel("../data_output/DS08_hiag_18.xlsx", index=False)
        i = input('\nVocê deseja atualizar algum outro dataset?\nDigite [S] ou [N]: ').upper()
    elif x == 9:
        # ATUALIZAR HISPANA 2019
        af_hiag_19 = "../data_input/PerformanceFinanceira/AF06_hispana_agrupados_19_20.xlsx"
        # Lendo a base e passando a lista com os missing values:
        af_hiag_19 = pd.read_excel(af_hiag_19, na_values=list_missingvalues)
        # renomear colunas
        af_hiag_19 = af_hiag_19.rename(columns=dict_columns)
        # filtrar uma coluna (série)
        af_hiag_19 = af_hiag_19[af_hiag_19['ANO'] == 2019]
        # descobrir o tipo de cada coluna
        print(af_hiag_19.dtypes)
        # descobrir número de linhas e colunas
        print(af_hiag_19.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(af_hiag_19.isnull().sum())
        # Enviando o arquivo gerado para uma pasta específica no computador
        af_hiag_19.to_excel("../data_output/DS09_hiag_19.xlsx", index=False)
        i = input('\nVocê deseja atualizar algum outro dataset?\nDigite [S] ou [N]: ').upper()
    elif x == 10:
        # ATUALIZAR HISPANA 2020
        af_hiag_20 = "../data_input/PerformanceFinanceira/AF07_hispana_agrupados_20_21.xlsx"
        # Lendo a base e passando a lista com os missing values:
        af_hiag_20 = pd.read_excel(af_hiag_20, na_values=list_missingvalues)
        # renomear colunas
        af_hiag_20 = af_hiag_20.rename(columns=dict_columns)
        # filtrar uma coluna (série)
        af_hiag_20 = af_hiag_20[af_hiag_20['ANO'] == 2020]
        # descobrir o tipo de cada coluna
        print(af_hiag_20.dtypes)
        # descobrir número de linhas e colunas
        print(af_hiag_20.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(af_hiag_20.isnull().sum())
        # Enviando o arquivo gerado para uma pasta específica no computador
        af_hiag_20.to_excel("../data_output/DS10_hiag_20.xlsx", index=False)
        i = input('\nVocê deseja atualizar algum outro dataset?\nDigite [S] ou [N]: ').upper()
    elif x == 12:
        # ATUALIZAR HISPANA 2021
        af_hiag_21 = "../data_input/PerformanceFinanceira/AF07_hispana_agrupados_20_21.xlsx"
        # Lendo a base e passando a lista com os missing values:
        af_hiag_21 = pd.read_excel(af_hiag_21, na_values=list_missingvalues)
        # renomear colunas
        af_hiag_21 = af_hiag_21.rename(columns=dict_columns)
        # filtrar uma coluna (série)
        af_hiag_21 = af_hiag_21[af_hiag_21['ANO'] == 2021]
        # descobrir o tipo de cada coluna
        print(af_hiag_21.dtypes)
        # descobrir número de linhas e colunas
        print(af_hiag_21.shape)
        # descobre a quantidade de valores ruins NaN nas colunas
        print(af_hiag_21.isnull().sum())
        # Enviando o arquivo gerado para uma pasta específica no computador
        af_hiag_21.to_excel("../data_output/DS11_hiag_21.xlsx", index=False)
        i = input('\nVocê deseja atualizar algum outro dataset?\nDigite [S] ou [N]: ').upper()
    else:
        print('\nOpção de atualização INVÁLIDA!')
print('\nFIM')
