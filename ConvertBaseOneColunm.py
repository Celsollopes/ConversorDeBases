
# coding: utf-8

# In[3]:


'''CONVERSOR DE DADOS PARA COLUNA UNICA - TRABALAHNDO COM SERIES TEMPORAIS'''

import pandas as pd


# In[23]:


#Recebe csv e cria nomes para as colunas
data = pd.read_csv('Saidas_PC_original.csv', delimiter=',', names=["Col-" + str(i) for i in range(48)])


# In[1]:


#data.head()


# In[25]:


data_formatted = pd.DataFrame(columns=['P'])#Cria um DataFrame com uma coluna chamada P


# In[27]:


#Pega os valores de (data) e add em data_formatted, cada linha abaixo da outra em uma coluna (P)
for i in range(len(data)):
    row = data.iloc[i].values
    data_formatted = data_formatted.append(pd.DataFrame(row))


# In[28]:


del data_formatted['P']


# In[29]:


data_formatted.to_csv("Saidas_PC_orignal_OneColumn.csv", index=False, header=None)#Salvando o arquivo como CSV

