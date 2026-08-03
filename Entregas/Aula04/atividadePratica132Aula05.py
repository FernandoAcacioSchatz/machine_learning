import numpy as np

alunos = np.array(
    [[17, 7.5, 90], [18, 8.0, 95], [19, 6.5, 70], [20, 9.0, 98], [21, 5.5, 65]]
)

print("Selecione alunos com nota maior ou igual a 7.")
notas = alunos[:, 1] >= 7
print(alunos[notas])
print("Selecione alunos com frequência menor que 75.")
frequencia = alunos[:, 2] < 75
print(alunos[frequencia])
print("Selecione alunos com idade maior que 18.")
idade = alunos[:, 0] > 18
print(alunos[idade])
print("Selecione alunos com nota maior ou igual a 7 e frequência maior ou igual a 75.")
notas_e_frequencia = (alunos[:, 1] >= 7) & (alunos[:, 2] >= 75)
print(alunos[notas_e_frequencia])
print("Selecione alunos com nota menor que 6 ou frequência menor que 70.")
notas_ou_frequencia = (alunos[:, 1] < 6) | (alunos[:, 2] < 70)
print(alunos[notas_ou_frequencia])
print("Conte quantos alunos possuem nota maior ou igual a 7.")
print(np.sum(alunos[:, 1] >= 7))
print("Verifique se existe algum aluno com frequência igual a 100.")
print(np.any(alunos[:, 2] == 100))
print("Verifique se todos os alunos possuem idade maior ou igual a 16.")
print(np.all(alunos[:, 0] >= 16))
