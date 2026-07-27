import numpy as np

dados = np.array([[17, 7.5, 90], [18, 8.0, 95], [19, 6.5, 70], [20, 9.0, 98]])

# 1. Qual é o tipo dos dados?
print(dados.dtype)
# 2. Qual é o formato do array?
print(dados.shape)
# 3. Quantas dimensões ele possui?
print(dados.ndim)
# 4. Quantos elementos existem no total?
print(dados.size)
# 5. Quantos alunos estão representados?
print(dados.shape[0])
# 6. Quantas features existem?
print(dados.shape[1])
