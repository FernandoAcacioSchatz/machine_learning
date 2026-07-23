import pandas as pd
import os
from tabulate import tabulate

# 1. Abrir `alunos_sujo.csv`
df = pd.read_csv(
    r"C:\Users\Fernando Acácio\OneDrive\Área de Trabalho\Entra21\Python\machine_learning\Aula 02\Aula02_Limpeza_Preparacao_Dados\datasets\sujos\alunos_sujo.csv"
)

dfc = df.copy()
print("DataFrame Original")
print(tabulate(dfc, headers="keys", tablefmt="psql", showindex=False))
print()

# 2. Mostrar as 5 primeiras linhas
print("5 primeiras linhas")
print(tabulate(dfc.head(), headers="keys", tablefmt="psql", showindex=False))
print()

# 3. Descobrir quantidade de linhas e colunas
print("Quantidade de linhas e colunas")
print(f"Quantidade de linhas: {len(dfc)}")
print(f"Quantidade de colunas: {dfc.shape[1]}")
print()

# 4. Verificar tipos de dados
print("Tipos de dados")
print(dfc.dtypes)
print()

# 5. Contar valores nulos
print("Valores nulos")
print(dfc.isnull().sum())
print()

# 6. Contar registros duplicados
print("Registros duplicados")
print(dfc.duplicated().sum())
print()

# **Parte 2 — Limpeza**
# 7. Preencher nota nula com a média
print("Preencher nota nula com a média")
media = round(dfc["Nota"].mean(), 1)
dfc["Nota"] = dfc["Nota"].fillna(media)
print(tabulate(dfc, headers="keys", tablefmt="psql", showindex=False))
print()

# 8. Preencher idade nula com a mediana
print("Preencher idade nula com a mediana")
medianaIdade = dfc["Idade"].median()
dfc["Idade"] = dfc["Idade"].fillna(medianaIdade)
print(tabulate(dfc, headers="keys", tablefmt="psql", showindex=False))
print()

# 9. Remover registros duplicados
print("Remover registros duplicados")
dfcDupli = dfc.drop_duplicates()
print(tabulate(dfcDupli, headers="keys", tablefmt="psql", showindex=False))
dfc = dfcDupli
print(tabulate(dfc, headers="keys", tablefmt="psql", showindex=False))
del dfcDupli
print()

# 10. Remover espaços extras da coluna `Nome`
print("Remover espaços extras da coluna `Nome`")
dfc["Nome"].str.strip()
print(tabulate(dfc, headers="keys", tablefmt="psql", showindex=False))
print()

# 11. Padronizar a coluna `Curso`
print("Padronizar a coluna `Curso`")
dfc["Curso"] = dfc["Curso"].str.title()

# 12. Corrigir idade negativa
print("Corrigir idade negativa")
dfc.loc[dfc["Idade"] < 0, "Idade"] = round(dfc["Idade"].median(), 0)
print(tabulate(dfc, headers="keys", tablefmt="psql", showindex=False))
print()

# 13. Corrigir nota acima de 10
print("Corrigir nota acima de 10")
dfc.loc[dfc["Nota"] > 10, "Nota"] = round(dfc["Nota"].mean(), 1)
print(tabulate(dfc, headers="keys", tablefmt="psql", showindex=False))
print()

# 14. Corrigir frequência acima de 100
print("Corrigir frequência acima de 100")
dfc.loc[dfc["Frequencia"] > 100, "Frequencia"] = round(dfc["Frequencia"].mean(), 0)
print(tabulate(dfc, headers="keys", tablefmt="psql", showindex=False))
print()

# 15. Converter `Data_Matricula` para data
print("Converter `Data_Matricula` para data")
print(dfc["Data_Matricula"].dtype)
dfc["Data_Matricula"] = pd.to_datetime(dfc["Data_Matricula"], format="mixed")

dfc["Data_Matricula"] = dfc["Data_Matricula"].dt.strftime("%d/%m/%Y")
print(tabulate(dfc, headers="keys", tablefmt="psql", showindex=False))
print()


# **Parte 3 — Entrega**

# 16. Verificar novamente valores nulos
print("Verificar novamente valores nulos")
print(dfc.isnull().sum())
print()

# 17. Verificar novamente duplicados
print("Verificar novamente duplicados")
print(dfc.duplicated().sum())
print()

# 18. Exibir `dfc.describe()`
print("dfc.describe()")
print(dfc.describe())
print()

# 19. Comparar DataFrame Original com DataFrame Tratado
print("Comparar DataFrame Original com DataFrame Tratado")
print("DataFrame Original")
print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))
print()
print("DataFrame Tratado")
print(tabulate(dfc, headers="keys", tablefmt="psql", showindex=False))
print("aqui")

# 19. Salvar como `alunos_tratado.csv`
df = dfc
caminho = r"C:\Users\Fernando Acácio\OneDrive\Área de Trabalho\Entra21\Python\machine_learning\Entregas\Aula02\csv_tratados\alunos_tratado.csv"

df.to_save(caminho, index=False)

print("Arquivo salvo" if os.path.exists(caminho) else "Falha ao salvar o arquivo")


# 20. Escrever três decisões tomadas durante a limpeza
print("Escrever três decisões tomadas durante a limpeza")
print(
    "1. Preencher valores nulos na coluna 'Nota' com a média das notas, para evitar perda de dados e manter a consistência da análise."
)
print(
    "2. Corrigir valores negativos na coluna 'Idade' substituindo-os pela mediana, garantindo que todas as idades sejam válidas e representativas."
)
print(
    "3. Padronizar a coluna 'Curso' para o formato de título, melhorando a legibilidade e consistência dos dados, facilitando futuras análises e relatórios."
)
print()
