import csv

# Nome do arquivo
arquivo_csv = "dados.csv"

# Ler o arquivo e armazenar os dados em uma lista
dados_lista = []
with open(arquivo_csv, mode="r", newline="", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)  # Pular o cabeçalho
    for linha in leitor:
        nome, idade = linha[0], int(linha[1])
        dados_lista.append((nome, idade))

# Pedir nome ao usuário
nome_digitado = input("Digite um nome: ")

# Verificar se o nome está na lista
encontrado = False
idades = [idade for _, idade in dados_lista]
mais_velho = max(idades)

for nome, idade in dados_lista:
    if nome.lower() == nome_digitado.lower():
        encontrado = True
        if idade == mais_velho:
            print(f"{nome} tem {idade} anos, é a pessoa mais velha da lista.")
        else:
            print(f"{nome} tem {idade} anos, não é a pessoa mais velha da lista.")
        break

if not encontrado:
    print("Nome não encontrado.")
