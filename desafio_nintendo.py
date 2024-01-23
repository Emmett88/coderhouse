import pandas as pd
from datetime import datetime, timedelta

# Essa parte deve abrir o arquivo em um dataframe
file_path = "/home/davidrangel/Desktop/py.coderhouse/best-selling-game-consoles.xlsx"

# isso lê o arquivo
df = pd.read_excel(file_path)

# aqui, deverá olhar as colunas do arquivo
expected_columns = ['Console', 'Name', 'Type', 'Company', 'Released Year', 'Discontinuation Year', 'Units sold (million)', 'Remarks']
if all(col in df.columns for col in expected_columns):
    # Substituir "NES" por "Nitendinho" e converter para maiúsculas
    df['Console'] = df['Console'].str.replace('NES', 'Nitendinho').str.upper()

    # isso é pra fazer a alteração da formatação da data
    df['Released Year'] = pd.to_datetime(df['Released Year'])

    # Isso é pra filtrar o ano
    df = df[df['Released Year'].dt.year > 2010]

    # aqui é para que eu consiga alterar a descrição
    df.describe(include='all')
    df.info()

    # aqui vai substituir o valores perdids
    df = df.fillna('missing')

    # Isso é para calcular a data da descontinuação
    df['Discontinuation Year'] = pd.to_datetime(df['Discontinuation Year'], errors='coerce')
    df['Discontinuation_Date'] = df['Released Year'] + timedelta(days=2*365)

    # Filtrar consoles descontinuados a menos de 2 anos da data de lançamento
    df = df[df['Discontinuation_Date'] > df['Released Year']]

    # Visualizar o dataframe resultante
    print(df)
else:
    print("As colunas esperadas não estão presentes no DataFrame.")
