import pandas as pd
from tabulate import tabulate

# 1. Abrir `alunos_sujo.csv`
df = pd.read_csv(
    r"C:\Users\Fernando Acácio\OneDrive\Área de Trabalho\Entra21\Python\machine_learning\Aula 02\Aula02_Limpeza_Preparacao_Dados\datasets\sujos\alunos_sujo.csv"
)
print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))
print()
# 2. Mostrar as 5 primeiras linhas
print(tabulate(df.head(), headers="keys", tablefmt="psql", showindex=False))
print()
# 3. Descobrir quantidade de linhas e colunas
print(f"Quantidade de linhas: {len(df)}")
print(f"Quantidade de colunas: {df.shape[1]}")
print()
# 4. Verificar tipos de dados
print(df.dtypes)
print()
# 5. Contar valores nulos
print(df.isnull().sum())
print()
# 6. Contar registros duplicados
print(df.duplicated().sum())
print()

# **Parte 2 — Limpeza**
# 7. Preencher nota nula com a média
media = round(df["Nota"].mean(), 1)
df["Nota"] = df["Nota"].fillna(media)
print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))
print()

# 8. Preencher idade nula com a mediana
medianaIdade = df["Idade"].median()
df["Idade"] = df["Idade"].fillna(medianaIdade)
print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))
print()
# 9. Remover registros duplicados
dfDupli = df.drop_duplicates()
print(tabulate(dfDupli, headers="keys", tablefmt="psql", showindex=False))
df = dfDupli
print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))
del dfDupli
print()

# 10. Remover espaços extras da coluna `Nome`
df["Nome"].str.strip()
print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))
print()

# 11. Padronizar a coluna `Curso`
df["Curso"] = df["Curso"].str.title()

# 12. Corrigir idade negativa
df.loc[df["Idade"] < 0, "Idade"] = round(df["Idade"].median(), 0)
print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))
print()
# 13. Corrigir nota acima de 10
df.loc[df["Nota"] > 10, "Nota"] = round(df["Nota"].mean(), 1)
print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))
print()

# 14. Corrigir frequência acima de 100
df.loc[df["Frequencia"] > 100, "Frequencia"] = round(df["Frequencia"].mean(), 0)
print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))
print()

# 15. Converter `Data_Matricula` para data
print(df["Data_Matricula"].dtype)
df["Data_Matricula"] = pd.to_datetime(df["Data_Matricula"], format="mixed")

df["Data_Matricula"] = df["Data_Matricula"].dt.strftime("%d/%m/%Y")
print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))
print()
