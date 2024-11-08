import pandas as pd
import numpy as np


def format_files(df_itau, df_kazah):

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)


    df_kazah = pd.read_excel('202307_FM_KAZAH.xlsx')

    # Selecionar as linhas relevantes a partir do cabeçalho (linha 18)
    header_row = 16
    df_kazah.columns = df_kazah.iloc[header_row]
    df_kazah = df_kazah.drop(range(header_row + 1))

    # Resetar o índice e remover colunas totalmente NaN (se presentes)
    df_kazah.reset_index(drop=True, inplace=True)
    df_kazah.dropna(axis=1, how='all', inplace=True)

    # Remover a coluna extra NaN e renomear as colunas
    df_kazah = df_kazah.drop(columns=[np.nan])
    df_kazah.columns = ['DATA', 'TRANSAÇÃO', 'CONTA', 'FORMA', 'PLANO DE CONTAS', 'VALOR', 'SALDO']

    # Forward fill the values in the column `DATA`
    df_kazah['DATA'] = df_kazah['DATA'].fillna(method='ffill')

    # Combine the values in the columns `TRANSAÇÃO` and `DATA`, where the values in `DATA` are null
    df_kazah['TRANSAÇÃO'] = np.where(df_kazah['TRANSAÇÃO'].isnull(), df_kazah['DATA'], df_kazah['TRANSAÇÃO'])

    # Remove the 'R$', '.', '+' and blank spaces from the column `VALOR` and replace ',' by '.'
    df_kazah['VALOR'] = df_kazah['VALOR'].astype(str).str.replace(r'[R$\.+ ]', '', regex=True).str.replace(',', '.', regex=False)

    # Remove rows with 'nan' values in `VALOR`
    df_kazah = df_kazah[df_kazah['VALOR'].astype(str).str.lower() != 'nan']

    # Convert the column `VALOR` to numeric
    df_kazah['VALOR'] = pd.to_numeric(df_kazah['VALOR'])

    df_kazah.to_csv('kazah_formatado.csv', index=False)

    # Formatação tabela itaú, apenas excluindo os valores nulos
    
    df_itau = pd.read_excel('Amais - Extrato Itaú julho.23.xlsx')

    df_itau = df_itau.drop(range(9))

    df_itau.columns = ['data', 'lançamento', 'ag./origem', 'valor (R$)', 'saldo (R$)']

    df_itau = df_itau[df_itau['valor (R$)'].notnull()]

    df_itau.to_csv('itau_formatado.csv', index=False)

