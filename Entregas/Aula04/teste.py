import numpy as np

nota = np.array([5.0, 6.5, 7.0, 8.5, 9.0])

print("Quantidade:", nota.size)
print("Soma:", np.sum(nota))
print("Média:", np.mean(nota))
print("Mediana:", np.median(nota))
print("Mínimo:", np.min(nota))
print("Máximo:", np.max(nota))
print("Desvio padrão:", np.std(nota))
print("Variância:", np.var(nota))

alunos = np.array([[18, 8.0, 90], [19, 6.5, 75], [20, 9.0, 98], [21, 7.5, 85]])

aluno_maior_nota = alunos[np.argmax(alunos[:, 1])]

print(aluno_maior_nota)

notas_decrescentes = alunos[np.argsort(alunos[:, 2])[::-1]]

print(notas_decrescentes)
