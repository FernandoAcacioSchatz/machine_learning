import numpy as np

X = np.array([[18, 8.0, 90], [19, 5.5, 65], [20, 9.0, 95]])

y = np.array([1, 0, 1])

novo_aluno = np.array([[20, 8.5, 92]])


# Qual é o shape?
print("Qual é o shape?")
print(X.shape)
print(y.shape)
print()
# Quantas dimensões possui?
print("Quantas dimensões possui?")
print(X.ndim)
print(y.ndim)
print()
# Por que o modelo pode recusar essa estrutura?
print(
    "Por que o modelo pode recusar essa estrutura?\nPorque o modelo espera uma matriz 2D para X e um vetor 1D para y"
)
print()
# Como transformar em uma matriz com uma linha?
print(
    "Como transformar em uma matriz com uma linha?\nAdicionando uma dimensão extra com colchetes"
)
# novo_aluno = np.array([[20, 8.5, 92]])
print()
# Como fazer isso utilizando colchetes?
print("Como fazer isso utilizando colchetes?")
# novo_aluno = np.array([[20, 8.5, 92]])
print()
# Como fazer isso utilizando reshape()?
print("Como fazer isso utilizando reshape()?")
print(np.array([20, 8.5, 92]).reshape(1, -1))
