import pandas as pd
from tabulate import tabulate

df = pd.read_csv(
    r"C:\Users\Fernando Acácio\OneDrive\Área de Trabalho\Entra21\Python\machine_learning\Aula 02\Aula02_Limpeza_Preparacao_Dados\datasets\sujos\alunos_sujo.csv"
)

# print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))

# print(df["Curso"])
dfAluno = df

dfAluno["Curso"] = dfAluno["Curso"].str.strip().title()
print(dfAluno["Curso"])

print(df["Curso"])
print(tabulate(dfAluno, headers="keys", tablefmt="grid", showindex=False))

df = dfAluno
print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))
