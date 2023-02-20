#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
from bs4 import BeautifulSoup

#Definindo o id do arquivo:
id = input('Qual o id?')

# Importando o arquivo CSV com código HTML:
df = pd.read_csv(r'C:\Users\lucas\Downloads\OBSERV.csv', encoding='iso-8859-1')

# Definindo a função RemoverHTML:
def RemoverHTML(texto):
    if isinstance(texto, str):
        soup = BeautifulSoup(texto, 'html.parser')
        return soup.get_text()
    else:
        return texto

# Aplicar a função a todos os elementos do DataFrame:
df = df.applymap(RemoverHTML)

# Exportar o arquivo sem HTML:
NomeArquivo = id + '.xlsx'
df.to_excel(NomeArquivo, index=False)

#Indicação de finalização:
print('Pronto!')




