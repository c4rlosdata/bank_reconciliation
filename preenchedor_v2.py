import pandas as pd

def sheet_filling():
    # Carregar e Preparar os Dados
    table1 = pd.read_csv('itau_formatado.csv')
    table2 = pd.read_csv('kazah_formatado.csv')
    valores_tabela2 = set(table2['VALOR'])
    table1['descricao'] = pd.NA

    # Lista para armazenar os índices usados
    indices_usados = set()

    # Combinar Valores Exatos
    for valor in valores_tabela2.copy():
        if valor in table1['valor (R$)'].values:
            transacao = table2.loc[table2['VALOR'] == valor, 'TRANSAÇÃO'].iloc[0]
            index = table2.loc[table2['VALOR'] == valor].index[0]
            if index not in indices_usados:
                table1.loc[table1['valor (R$)'] == valor, 'descricao'] = transacao
                indices_usados.add(index)
                valores_tabela2.remove(valor)

    # Lista para armazenar valores a serem removidos
    valores_para_remover = []

    # Procurar Combinações de 2 Valores
    for k, valor_1 in enumerate(table1['valor (R$)']):
        if pd.isna(table1.at[k, 'descricao']):
            for valor_2 in valores_tabela2:
                diferenca = valor_1 - valor_2
                if diferenca in valores_tabela2:
                    index1 = table2.loc[table2['VALOR'] == valor_2].index[0]
                    index2 = table2.loc[table2['VALOR'] == diferenca].index[0]
                    if index1 not in indices_usados and index2 not in indices_usados:
                        transacao1 = table2.loc[table2['VALOR'] == valor_2, 'TRANSAÇÃO'].iloc[0]
                        transacao2 = table2.loc[table2['VALOR'] == diferenca, 'TRANSAÇÃO'].iloc[0]
                        table1.at[k, 'descricao'] = f"{transacao1} + {transacao2}"

                        valores_para_remover.append(valor_2)
                        valores_para_remover.append(diferenca)
                        indices_usados.add(index1)
                        indices_usados.add(index2)

                        break

    # Procurar Combinações de 3 Valores
    for k, valor_1 in enumerate(table1['valor (R$)']):
        if pd.isna(table1.at[k, 'descricao']):
            for valor_2 in valores_tabela2:
                for valor_3 in valores_tabela2:
                    diferenca_tres = valor_1 - valor_2 - valor_3
                    if diferenca_tres in valores_tabela2:
                        index1 = table2.loc[table2['VALOR'] == valor_2].index[0]
                        index2 = table2.loc[table2['VALOR'] == valor_3].index[0]
                        index3 = table2.loc[table2['VALOR'] == diferenca_tres].index[0]
                        if index1 not in indices_usados and index2 not in indices_usados and index3 not in indices_usados:
                            transacao1 = table2.loc[table2['VALOR'] == valor_2, 'TRANSAÇÃO'].iloc[0]
                            transacao2 = table2.loc[table2['VALOR'] == valor_3, 'TRANSAÇÃO'].iloc[0]
                            transacao3 = table2.loc[table2['VALOR'] == diferenca_tres, 'TRANSAÇÃO'].iloc[0]
                            table1.at[k, 'descricao'] = f"{transacao1} + {transacao2} + {transacao3}"

                            valores_para_remover.append(valor_2)
                            valores_para_remover.append(valor_3)
                            valores_para_remover.append(diferenca_tres)
                            indices_usados.add(index1)
                            indices_usados.add(index2)
                            indices_usados.add(index3)

                            break
                if not pd.isna(table1.at[k, 'descricao']):
                    break

    # Procurar Combinações de 4 Valores
    for k, valor_1 in enumerate(table1['valor (R$)']):
        if pd.isna(table1.at[k, 'descricao']):
            for valor_2 in valores_tabela2:
                for valor_3 in valores_tabela2:
                    for valor_4 in valores_tabela2:
                        diferenca_quatro = valor_1 - valor_2 - valor_3 - valor_4
                        if diferenca_quatro in valores_tabela2:
                            index1 = table2.loc[table2['VALOR'] == valor_2].index[0]
                            index2 = table2.loc[table2['VALOR'] == valor_3].index[0]
                            index3 = table2.loc[table2['VALOR'] == valor_4].index[0]
                            index4 = table2.loc[table2['VALOR'] == diferenca_quatro].index[0]
                            if index1 not in indices_usados and index2 not in indices_usados and index3 not in indices_usados and index4 not in indices_usados:
                                transacao1 = table2.loc[table2['VALOR'] == valor_2, 'TRANSAÇÃO'].iloc[0]
                                transacao2 = table2.loc[table2['VALOR'] == valor_3, 'TRANSAÇÃO'].iloc[0]
                                transacao3 = table2.loc[table2['VALOR'] == valor_4, 'TRANSAÇÃO'].iloc[0]
                                transacao4 = table2.loc[table2['VALOR'] == diferenca_quatro, 'TRANSAÇÃO'].iloc[0]
                                table1.at[k, 'descricao'] = f"{transacao1} + {transacao2} + {transacao3} + {transacao4}"

                                valores_para_remover.append(valor_2)
                                valores_para_remover.append(valor_3)
                                valores_para_remover.append(valor_4)
                                valores_para_remover.append(diferenca_quatro)
                                indices_usados.add(index1)
                                indices_usados.add(index2)
                                indices_usados.add(index3)
                                indices_usados.add(index4)

                                break
                    if not pd.isna(table1.at[k, 'descricao']):
                        break
                if not pd.isna(table1.at[k, 'descricao']):
                    break

    # Remover valores utilizados após os loops
    for valor in set(valores_para_remover):
        valores_tabela2.remove(valor)

    # Salvar em Excel
    with pd.ExcelWriter("planilha_principal_v2.xlsx") as writer:
        table1.to_excel(writer, sheet_name="Tabela 1", index=False, columns=['data', 'lançamento', 'ag./origem', 'valor (R$)', 'descricao'])
        table2.to_excel(writer, sheet_name="Tabela 2", index=False)

