import pandas as pd
from tabulate import tabulate

df = pd.read_csv(
    r"C:\Users\Fernando Acácio\OneDrive\Área de Trabalho\Entra21\Python\machine_learning\Aula 01\Aula01_Machine_Learning\livros.csv"
)

print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))

print(f"Quantidade de linhas: {len(df)}")
print(f"Quantidade de colunas: {df.shape[1]}")
livroMaisAntigo = df.loc[df["Ano"].idxmin()]
print(f"Livro mais antigo: {livroMaisAntigo['Titulo']} ({livroMaisAntigo['Ano']})")
maiorNrPaginas = df.loc[df["Paginas"].idxmax()]
print(
    f"Livro com maior número de páginas: {maiorNrPaginas['Titulo']} ({maiorNrPaginas['Paginas']})"
)
autor = df["Autor"].unique().tolist()
print(*autor, sep=", ", end="")
