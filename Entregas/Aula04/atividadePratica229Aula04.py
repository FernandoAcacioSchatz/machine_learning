import numpy as np

notas = np.array([4.5, 5.5, 6.0, 7.0, 8.5, 9.0, 10.0])

np.set_printoptions(precision=2)

print("1. soma;")
soma = np.sum(notas)
print(soma)
print()

print("2. média;")
media = np.mean(notas)
print(media)
print()

print("3. mediana;")
mediana = np.median(notas)
print(mediana)
print()

print("4. mínimo;")
minino = np.min(notas)
print(minino)
print()

print("5. máximo;")
maximo = np.max(notas)
print(maximo)
print()

print("6. amplitude;")
amplitude = np.max(notas) - np.min(notas)
print(amplitude)
print()


print("7. desvio padrão;")
desvioPadrao = np.std(notas)
print(desvioPadrao)
print()

print("8. variância;")
variancia = np.var(notas)
print(variancia)
print()

print("9. primeiro quartil;")
primeiroQuartil = np.percentile(notas, 25)
print(primeiroQuartil)
print()

print("10. terceiro quartil.")
terceiroQuartil = np.percentile(notas, 75)
print(terceiroQuartil)
print()
