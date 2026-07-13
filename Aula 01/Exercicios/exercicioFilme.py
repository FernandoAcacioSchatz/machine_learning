import pandas as pd
from tabulate import tabulate

df = pd.read_csv(
    r"C:\Users\Fernando Acácio\OneDrive\Área de Trabalho\Entra21\Python\machine_learning\Aula 01\Aula01_Machine_Learning\filmes.csv",
    sep=" ",
)

print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))
