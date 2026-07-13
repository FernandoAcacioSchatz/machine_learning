import pandas as pd
from tabulate import tabulate

df = pd.read_csv(
    r"C:\Users\Fernando Acácio\OneDrive\Área de Trabalho\Entra21\Python\machine_learning\Aula 02\Aula02_Limpeza_Preparacao_Dados\datasets\sujos\alunos_sujo.csv"
)

print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))
# print(df.duplicated().sum())
# print(df[df.duplicated()])


print("Linhas e Colunas")
print(df.shape)
print()
print("Primeiras Linhas")
print(df.head())
print()
print("")
print(df.tail())
print()
print("Nome das colunas")
print(df.columns)
print()
print("Tipos das colunas")
print(df.dtypes)
print()
print("Resumo do DataFrame")
print(df.info())
print()
print("Estatisticas descritivas")
print(df.describe())
print()
print("Cria tabela com valores nulos")
print(df.isnull().sum())
print()
print(
    "Retorna uma série de valores booleanos indicando se cada linha é uma duplicata de uma linha anterior."
)
print(df.duplicated().sum())
print()
print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))
print()
# quero tratar valores nulos.
# Média da coluna Nota
media_nota = df["Nota"].mean()
print("Média:", media_nota)
print()
print(f"Média: {df['Nota'].mean()}")
# Preenche as notas ausentes com a média
df["Nota"] = df["Nota"].fillna(media_nota)
print()
# Preenche idade ausente com a mediana
mediana_idade = df["Idade"].median()
df["Idade"] = df["Idade"].fillna(mediana_idade)
print()
# Confere se os nulos foram tratados
df.isnull().sum()
print()
print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))
print()


# Média da coluna Nota
media_nota = df["Nota"].mean()
print("Média:", media_nota)
print()
# Preenche as notas ausentes com a média
df["Nota"] = df["Nota"].fillna(media_nota)
print()

# Preenche idade ausente com a mediana
mediana_idade = df["Idade"].median()
df["Idade"] = df["Idade"].fillna(mediana_idade)
print()
# Confere se os nulos foram tratados
df.isnull().sum()
print()
print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))
print()
# Mostra apenas os registros duplicados
df[df.duplicated()]
print()
# Remove registros completamente repetidos
df = df.drop_duplicates()
print("Duplicados restantes:", df.duplicated().sum())
print()
# corrigundo tipos de dados
df["Idade"] = pd.to_numeric(df["Idade"], errors="coerce")
df["Nota"] = pd.to_numeric(df["Nota"], errors="coerce")
df["Frequencia"] = pd.to_numeric(df["Frequencia"], errors="coerce")
print()
df["Data_Matricula"] = pd.to_datetime(
    df["Data_Matricula"], dayfirst=True, errors="coerce"
)
# padronizando data
df["Data_Matricula"] = df["Data_Matricula"].fillna(pd.to_datetime("2020-01-01"))
print()
df.dtypes
print()
# localizando valores invalidos
# Idades negativas
df[df["Idade"] < 0]
print()
# Notas acima de 10
df[df["Nota"] > 10]
print()
# Frequências acima de 100
df[df["Frequencia"] > 100]
print()
# 9. Corrigindo valores inválidos
# As decisões abaixo são didáticas. Em projetos reais, consulte as regras do negócio.
# Troca idades negativas pela mediana das idades válidas
idade_mediana_valida = int(df[df["Idade"] >= 0]["Idade"].median())
df.loc[df["Idade"] < 0, "Idade"] = idade_mediana_valida
print()
# Limita a nota máxima a 10
df.loc[df["Nota"] > 10, "Nota"] = 10
print()
# Limita a frequência máxima a 100
df.loc[df["Frequencia"] > 100, "Frequencia"] = 100
print()

# Converte a coluna Data_Matricula para datetime
df["Data_Matricula"] = pd.to_datetime(df["Data_Matricula"], errors="coerce")

# Preenche valores nulos
df["Idade"] = df["Idade"].fillna(df["Idade"].mean())
df["Nota"] = df["Nota"].fillna(df["Nota"].mean())
df["Frequencia"] = df["Frequencia"].fillna(df["Frequencia"].mean())

# Preenche datas nulas
df["Data_Matricula"] = df["Data_Matricula"].fillna(pd.Timestamp("2020-01-01"))

# Remove horário e deixa no formato brasileiro
df["Data_Matricula"] = df["Data_Matricula"].dt.strftime("%d/%m/%Y")

# Remove linhas duplicadas
df = df.drop_duplicates()

print()
print("DATASET LIMPO")
print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))
print()
