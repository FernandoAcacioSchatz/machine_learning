import pandas as pd
from tabulate import tabulate

df = pd.read_csv(
    r"C:\Users\Fernando Acácio\OneDrive\Área de Trabalho\Entra21\Python\machine_learning\Aula 01\Aula01_Machine_Learning\filmes.csv"
)

print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))
print(f"Quantidade de linhas: {len(df)}")
print(f"Quantidade de colunas: {df.shape[1]}")
filmeMaisAntigo = df.loc[df["Ano"].idxmin()]
print(f"Filme mais antigo: {filmeMaisAntigo['Filme']} ({filmeMaisAntigo['Ano']})")
maiorIMDb = df.loc[df["NotaIMDb"].idxmax()]
print(f"Filme com maior IMDb: {maiorIMDb['Filme']} ({maiorIMDb['NotaIMDb']})")
generos = df["Genero"].unique().tolist()
print(*generos, sep=", ", end="")
