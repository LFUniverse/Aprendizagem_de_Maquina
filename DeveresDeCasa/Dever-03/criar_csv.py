import csv

# Dados a serem escritos no arquivo
dados = [
    ["Nome", "Idade"],
    ["Ana", 25],
    ["Bruno", 30],
    ["Carla", 22],
    ["Daniel", 28],
    ["Eduardo", 35]
]

# Nome do arquivo
arquivo_csv = "dados.csv"

# Escrevendo no arquivo CSV
with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)

print(f"Arquivo '{arquivo_csv}' criado com sucesso!")
