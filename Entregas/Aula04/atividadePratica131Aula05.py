import numpy as np

alunos = np.array(
    [[17, 7.5, 90], [18, 8.0, 95], [19, 6.5, 70], [20, 9.0, 98], [21, 5.5, 65]]
)


print("Acesse o primeiro aluno.")
print(alunos[0])
print("Acesse o último aluno.")
print(alunos[-1])
print("Acesse a nota do segundo aluno.")
print(alunos[1, 1])
print("Acesse a frequência do quarto aluno.")
print(alunos[3, 2])
print("Selecione todas as idades.")
print(alunos[:, 0])
print("Selecione todas as notas.")
print(alunos[:, 1])
print("Selecione todas as frequências.")
print(alunos[:, 2])
print("Selecione os três primeiros alunos.")
print(alunos[:3])
print("Selecione nota e frequência de todos os alunos.")
print(alunos[:3, 1:])
print("Selecione idade e frequência, ignorando a nota.")
print(alunos[:, [0, 2]])
