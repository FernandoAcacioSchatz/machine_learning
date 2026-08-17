import numpy as np

dados = np.array([[18, 8.0, 90], [19, 6.0, 70], [20, 9.0, 98], [21, 7.0, 85]])

np.set_printoptions(precision=2)

print("1. Calcule a média de todos os valores.")
media = np.mean(dados)
print(media)
print()

print("2. Calcule a média por coluna.")
mediaPorColuna = np.mean(dados, axis=0)
print(mediaPorColuna)
print()

print("3. Calcule a soma por coluna.")
somaMEdiaPorColuna = np.sum(dados, axis=0)
print(somaMEdiaPorColuna)
print()

print("4. Calcule o mínimo por coluna.")
minimoPorColuna = np.min(dados, axis=0)
print(minimoPorColuna)
print()

print("5. Calcule o máximo por coluna.")
maximoPorColuna = np.max(dados, axis=0)
print(maximoPorColuna)
print()

print("6. Calcule o desvio padrão por coluna.")
desvioPadraoPorColuna = np.std(dados, axis=0)
print(desvioPadraoPorColuna)
print()

print("7. Expliqeu o significado de cada resultado.")


print("8. Calcule a média por linha.")
mediaPorLinha = np.mean(dados, axis=1)
print(mediaPorLinha)
print()


print("9. Explique por que a média por linha não é adequada nesse exemplo.")
print(
    "A média por linha não é adequada nesse exemplo porque cada linha representa um conjunto de dados diferentes (idade, nota e frequência), e calcular a média desses valores juntos não faz sentido estatisticamente. Cada coluna deve ser analisada separadamente para obter informações significativas.\n"
)
print("10. Extraia somente nota e frequência e calcule as médias.")
nota = dados[:, 1]
frequencia = dados[:, 2]
mediaNota = np.mean(nota)
mediaFrequencia = np.mean(frequencia)
print(f"Média das notas: {mediaNota}")
print(f"Média das frequências: {mediaFrequencia}")
