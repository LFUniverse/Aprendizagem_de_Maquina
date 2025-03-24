import pandas as pd
import random

# Criando a lista de frutas com repetições
frutas = ["maçã", "banana", "laranja", "uva", "maçã", "melão", "mamão", "banana"]

# Criando um dicionário para armazenar as quantidades
quantidades = {fruta: random.randint(0, 100) for fruta in frutas}

# Escrevendo no arquivo minhas_frutas.txt
with open("minhas_frutas.txt", "w") as f:
    for fruta, quantidade in quantidades.items():
        f.write(f"{fruta},{quantidade}\n")

# Lendo o arquivo e somando as quantidades
dados = {}
with open("minhas_frutas.txt", "r") as f:
    for linha in f:
        fruta, quantidade = linha.strip().split(",")
        quantidade = int(quantidade)
        if fruta in dados:
            dados[fruta] += quantidade
        else:
            dados[fruta] = quantidade

# Criando um DataFrame com os dados
df = pd.DataFrame(list(dados.items()), columns=["Fruta", "Quantidade"])

# Exibindo o DataFrame
print(df)