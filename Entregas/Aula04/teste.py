import numpy as np

notas = np.array([5.5, 7.0, 8.5, 9.0])

print("Notas originais:")
print(notas)

notas_atualizadas = np.clip(notas - 6, 0, 10)

print(notas_atualizadas)
