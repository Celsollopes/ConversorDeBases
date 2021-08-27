
# coding: utf-8

'''CONVERSOR DE DADOS LINHA PARA COLUNA UNICA - TRABALAHNDO COM SERIES TEMPORAIS'''

import pandas as pd

#Recebe csv e cria nomes para as colunas
data = pd.read_csv('Saidas_PC_original.csv', delimiter=',', names=["Col-" + str(i) for i in range(48)])

data_formatted = pd.DataFrame(columns=['P'])#Cria um DataFrame com uma coluna chamada P

#Pega os valores de (data) e add em data_formatted, cada linha abaixo da outra em uma coluna (P)
for i in range(len(data)):
    row = data.iloc[i].values
    data_formatted = data_formatted.append(pd.DataFrame(row))

#del data_formatted['P']

data_formatted.to_csv("Saidas_PC_orignal_OneColumn.csv", index=False, header=None)#Salvando o arquivo como CSV

