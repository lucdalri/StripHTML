import pandas as pd
from pandas.io.formats import excel
from bs4 import BeautifulSoup

#Definindo a identificação do arquivo:
id = input('Qual o id?')

# Definindo a função RemoverHTML:
def RemoverHTML(texto):
    if isinstance(texto, str):
        soup = BeautifulSoup(texto, 'html.parser')
        return soup.get_text()
    else:
        return texto

# Importando o arquivo CSV com código HTML:
df = pd.read_csv(r'CAMINHO DO ARQUIVO', encoding='iso-8859-1')

#Remover formato da Header
excel.ExcelFormatter.header_style = None

# Aplicar a função a todos os elementos do DataFrame:
df = df.applymap(RemoverHTML)

# Exportar o arquivo em formato excel sem entidades HTML:
NomeArquivo = id + '.xlsx'
df.to_excel(NomeArquivo, engine = 'xlsxwriter'  index=False)

#Indicação de finalização:
print('Pronto!')
