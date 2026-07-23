import pandas as pd

filmes = []

for i in range(5):
    print(f"\nCadastro do {i + 1}º filme")

    nome = input("Nome do filme: ")
    ano = int(input("Ano: "))
    genero = input("Gênero: ")
    nota = float(input("Nota IMDb: "))
    duracao = int(input("Duração (min): "))

    filmes.append(
        {
            "Filme": nome,
            "Ano": ano,
            "Gênero": genero,
            "Nota IMDb": nota,
            "Duração": duracao,
        }
    )

df = pd.DataFrame(filmes)

print("\nFilmes cadastrados:")
print(df)
