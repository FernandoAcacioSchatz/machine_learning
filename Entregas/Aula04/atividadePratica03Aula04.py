import numpy as np

X = np.array([[18, 8.0, 90], [19, 5.5, 65], [20, 9.0, 95]])

y = np.array([1, 0])


# 1. Qual é o problema?
print("Qual é o problema?\nO problema encontrado é a falta de uma target")
# 2. Qual é o formato de `X`?
print("Qual é o formato de `X`?")
print(X.dtype)
print(X.shape)
# 3. Qual é o formato de `y`?
print("Qual é o formato de `y`?")
print(y.dtype)
print(y.shape)
# 4. Como corrigir?
print("Como corrigir?\nIncluindo em y mais uma target")
# 5. Qual erro pode aparecer no treinamento?
print(
    "Qual erro pode aparecer no treinamento?\nO erro que pode aparecer é a falta de uma target no y"
)
