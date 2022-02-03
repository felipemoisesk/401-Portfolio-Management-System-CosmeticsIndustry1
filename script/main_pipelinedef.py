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
list_missingvalues = [' -   ',
                      '  -    ',
                      '-'
                      ]

year_date = int(input('Qual ANO deseja atualizar?: '))
name_file = input('Qual PAÍS deseja atualizar?: ').lower()
chan_file = input('Qual CANAL deseja atualizar?: ').lower()
exte_file = input('Digite a o NOME que deseja para o arquivo de saída: ').lower()
path = r'../data_input/PerformanceFinanceira/'
path_destino = r'../data_output/'
type_file = 'xlsx'


def read_file(path, year_date, name_file, chan_file, type_file):
    file = f'{path}{year_date}99_{name_file}_{chan_file}.{type_file}'
    df = pd.read_excel(file, na_values=list_missingvalues)
    return df

def rename_stocks(df):
    df = df.rename(columns=dict_columns)
    return df

def filter_stocks(df):
    df = df[df['ANO'] == year_date]
    return df

def save_file(path, year_date, name_file, chan_file, type_file, path_destino, exte_file):
    df = read_file(path, year_date, name_file, chan_file, type_file)
    df = rename_stocks(df)
    df = filter_stocks(df)
    df.to_excel(f'{path_destino}{year_date}99_{exte_file}.{type_file}', index=False)

save_file(path, year_date, name_file, chan_file, type_file, path_destino, exte_file)

