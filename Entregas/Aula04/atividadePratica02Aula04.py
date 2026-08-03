import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from tabulate import tabulate

df = pd.DataFrame(
    {
        "Idade": [18, 19, 20, 21, 22],
        "Nota": [8.0, 5.5, 9.0, 6.5, 7.5],
        "Frequencia": [90, 65, 95, 75, 85],
        "Aprovado": [1, 0, 1, 0, 1],
    }
)

print(df)
print("aqui")

X = df[["Idade", "Nota", "Frequencia"]]
y = df["Aprovado"]

# 1. verifique X.shape
print(X.shape)
# 2. verifique y.shape
print(y.shape)
# 3. confirme se as quantidades de amostras são iguais;
print(X.shape[0])
print(y.shape[0])

# 4. treine uma Árvore de Decisão;
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42
)
modelo_arvore = DecisionTreeClassifier(random_state=42)
modelo_arvore.fit(X_treino, y_treino)
print("Modelo de Árvore de Decisão treinado com sucesso!")
# 5. faça uma previsão para um novo aluno.
novoAluno = [[34, 7.5, 80]]

previsao = modelo_arvore.predict(novoAluno)
print(previsao)
