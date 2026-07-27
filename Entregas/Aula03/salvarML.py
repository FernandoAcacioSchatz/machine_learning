import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

from tabulate import tabulate
from sklearn.datasets import load_iris
import joblib

# ESSA LINHA CRIA A VARIÁVEL 'dados':
dados = load_iris()

df = pd.read_csv(
    r"C:\Users\Fernando Acácio\OneDrive\Área de Trabalho\Entra21\Python\machine_learning\Aula 02\Aula02_Limpeza_Preparacao_Dados\datasets\gabarito\clientes_tratado.csv"
)
print(tabulate(df, headers="keys", tablefmt="grid"))

X = df[["Idade", "Renda"]]
y = df["Comprou"]

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = DecisionTreeClassifier()
modelo.fit(X_treino, y_treino)

previsoes = modelo.predict(X_teste)
acuracia = accuracy_score(y_teste, previsoes)

print(f"Acurácia: {acuracia:.2%}")

print("\nRelatório de Classificação:")
print(classification_report(y_teste, previsoes))

plt.figure(figsize=(15, 8))
plot_tree(
    modelo,
    feature_names=X.columns,
    class_names=["Não", "Sim"],
    filled=True,
    fontsize=10,
)
plt.show()

for coluna, importancia in zip(X.columns, modelo.feature_importances_):
    print(coluna, importancia)

joblib.dump(modelo, "clientes_aprovacao.pkl")
