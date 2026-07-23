# Escreva um pequeno relatório contendo.
import pandas as pd
from tabulate import tabulate

df = pd.read_csv(
    r"C:\Users\Fernando Acácio\OneDrive\Área de Trabalho\Entra21\Python\machine_learning\Aula 01\Aula01_Machine_Learning\alunos.csv"
)
print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))

# quantidade de registros;
print("Quantidade de registros:", df.shape[0])


# quantidade de colunas;
print(f"Quantidade de colunas: {df.shape[1]}")

# nomes das colunas;
print("Nome das colunas:", ", ".join(df.columns))

# média da nota;
print("Média da nota:", round(df["Nota"].mean(), 2))

# menor nota;
menorNota = df.loc[df["Nota"].idxmin()]
print(f"Menor nota: {menorNota["Nome"]} ({menorNota['Nota']})")

# maior nota.
maiorNota = df.loc[df["Nota"].idxmax()]
print(f"Maior nota: {maiorNota['Nome']} ({maiorNota['Nota']})")
