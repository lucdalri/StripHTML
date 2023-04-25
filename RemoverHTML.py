import pandas as pd
from pandas.io.formats import excel
from bs4 import BeautifulSoup

# Definindo a identificação do arquivo:
id = input('Qual o nome do arquivo de destino?')

# Definindo a função RemoverHTML:
def RemoverHTML(texto):
    if isinstance(texto, str):
        soup = BeautifulSoup(texto, 'html.parser')
        return soup.get_text()
    else:
        return texto

# Importando o arquivo CSV com código HTML:
# 1. Descrever o caminho de destino
# 2. Definir o separador de colunas (Exemplo: vírgula (','), dois-pontos (':'), ponto-e-vírgula (';'), entre outros conforme a planilha a ser utilizada.
# 3. Definir o encoding do arquivo, seja ele ISO-8859-1, UTF8, etc.
df = pd.read_csv(r'<CAMINHO DO ARQUIVO>', sep ='<SEPARADOR>', engine ='python', encoding = ('<ENCODING>')

# Remover formatação da Header
excel.ExcelFormatter.header_style = None

# Aplicar a função a todos os elementos do DataFrame:
df = df.applymap(RemoverHTML)

# Exportar o arquivo em formato excel sem entidades HTML:
NomeArquivo = id + '.xlsx'
df.to_excel(NomeArquivo, engine = 'xlsxwriter'  index=False)

# Indicação de finalização:
print('Pronto!')
