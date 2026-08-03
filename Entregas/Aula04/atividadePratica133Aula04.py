import numpy as np

notas = np.array([7.5, -1.0, 8.5, 11.0, np.nan, 6.0])

print(notas)
print("Identifique notas menores que zero.")
notaMenorZero = notas[notas < 0]
print(notaMenorZero)
print("Identifique notas maiores que dez.")
notaMaiorDez = notas[notas > 10]
print(notaMaiorDez)
print("Conte os valores ausentes.")
print(np.sum(np.isnan(notas)))
print("Selecione somente notas válidas.")
print(notas)
notaValida = notas[~np.isnan(notas)]
print(notaValida)
print("Corrija valores menores que zero para zero.")
print(notas)
notaCorrigida = np.clip(notas, 0, 10)
print(notaCorrigida)
print("Corrija valores maiores que dez para dez.")
print(notas)
notaCorrigida = np.clip(notas, 0, 10)
print(notaCorrigida)
print("Substitua o valor ausente pela média das notas válidas.")
print(notas)
notaMedia = np.mean(notaValida)
notas[np.isnan(notas)] = notaMedia
notaCorrigida = np.clip(notas, 0, 10)
print(notaCorrigida)
print("Calcule a média final.")
mediaFinal = np.mean(notaCorrigida)
print(f"{mediaFinal:.2f}")
