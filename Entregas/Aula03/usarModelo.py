import joblib
import pandas as pd
from tabulate import tabulate

df = pd.read_csv(
    r"C:\Users\Fernando Acácio\OneDrive\Área de Trabalho\Entra21\Python\machine_learning\Aula 02\Aula02_Limpeza_Preparacao_Dados\datasets\gabarito\clientes_tratado.csv"
)

print(tabulate(df, headers="keys", tablefmt="grid"))

modelo = joblib.load(
    r"C:\Users\Fernando Acácio\OneDrive\Área de Trabalho\Entra21\Python\machine_learning\clientes_aprovacao.pkl"
)

novo_cliente = [[28, 5000]]

resultado = modelo.predict(novo_cliente)

print(resultado)
