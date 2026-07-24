import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

from tabulate import tabulate

df = pd.read_csv(
    r"C:\Users\Fernando Acácio\OneDrive\Área de Trabalho\Entra21\Python\machine_learning\Aula 03\Aula03_Primeiro_Modelo_ML\datasets\alunos_tratado.csv"
)

print(tabulate(df, headers="keys", tablefmt="psql"))

X = df[["Idade", "Nota", "Frequencia"]]
y = df["Aprovado"]

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = DecisionTreeClassifier()

modelo.fit(X_treino, y_treino)

previsoes = modelo.predict(X_teste)

acuracia = accuracy_score(y_teste, previsoes)
print(f"Acurácia do modelo: {acuracia * 100:.2f}%")

print("\nRelatório de Classificação:")
print(classification_report(y_teste, previsoes))

plt.figure(figsize=(15, 8))
plot_tree(modelo, feature_names=X.columns, class_names=["Não", "Sim"], filled=True)
plt.show()

for coluna, importancia in zip(X.columns, modelo.feature_importances_):
    print(coluna, importancia)
