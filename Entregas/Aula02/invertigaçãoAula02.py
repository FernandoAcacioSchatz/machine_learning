import pandas as pd
from tabulate import tabulate

# **Parte 1 — Investigação**
# 1. Abrir `alunos_sujo.csv`
df = pd.read_csv(
    r"C:\Users\Fernando Acácio\OneDrive\Área de Trabalho\Entra21\Python\machine_learning\Aula 02\Aula02_Limpeza_Preparacao_Dados\datasets\sujos\alunos_sujo.csv"
)
print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))

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
