import numpy as np

valores = np.array([10, 20, 30, 40, 50])

np.set_printoptions(precision=2)


print("1. Some 5 a todos os valores.")
somaCinco = valores + 5
print(somaCinco)
print()

print("2. Subtraia 10 de todos os valores.")
subtraiDez = valores - 10
print(subtraiDez)
print()

print("3. Multiplique todos os valores por 3.")
multiplicaTres = valores * 3
print(multiplicaTres)
print()

print("4. Divida todos os valores por 10.")
divideDez = valores / 10
print(divideDez)
print()

print("5. Eleve todos os valores ao quadrado.")
elevaQuadrado = valores**2
print(elevaQuadrado)
print()

print("6. Calcule a raiz quadrada.")
raizQuadrada = np.sqrt(valores)
print(raizQuadrada)
print()

print("7. Calcule a soma total.")
somaTotal = np.sum(valores)
print(somaTotal)
print()

print("8. Calcule a média.")
media = np.mean(valores)
print(media)
print()

print("9. Encontre o menor valor.")
menorValor = np.min(valores)
print(menorValor)
print()

print("10. Encontre o maior valor.")
maiorValor = np.max(valores)
print(maiorValor)
print()
