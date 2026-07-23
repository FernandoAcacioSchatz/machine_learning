# Importar o Pandas
import pandas as pd
import os
from tabulate import tabulate

# Upload do arquivo `alunos.csv`
# Ler com `pd.read_csv()`
df = pd.read_csv(
    r"C:\Users\Fernando Acácio\OneDrive\Área de Trabalho\Entra21\Python\machine_learning\Aula 01\Aula01_Machine_Learning\alunos.csv"
)
# Rodar `os.listdir()` para confirmar
arquivos = os.listdir()

# Exibir a tabela
print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))
print(arquivos)
