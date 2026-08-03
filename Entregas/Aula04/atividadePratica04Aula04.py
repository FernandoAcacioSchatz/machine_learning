import numpy as np

np.set_printoptions(precision=2, suppress=True)

np.random.seed(42)

idades = np.random.randint(16, 51, size=20)
notas = np.round(np.random.uniform(0, 10, size=20) * 2) / 2
frequencias = np.random.randint(50, 101, size=20)

X = np.column_stack((idades, notas, frequencias))

y = np.where((notas >= 7) & (frequencias >= 75), 1, 0)

print(X)
print(y)
print(X.shape)
print(y.shape)
