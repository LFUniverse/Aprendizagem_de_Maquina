# Lista com elementos fornecidos
itens = ["Carro", "Abajur", "Moto", "Barco", "Ferro de passar roupa", "2", "Barco", "moto"]

# Remover elementos duplicados convertendo para um conjunto
itens_unicos = list(set(itens))

# Ordenar considerando maiúsculas, minúsculas e números corretamente
itens_unicos.sort(key=lambda x: (str(x).lower(), x))

# Nome do arquivo
arquivo = "lista_Desafio.txt"

# Gravar os elementos únicos e ordenados no arquivo
with open(arquivo, "w", encoding="utf-8") as f:
    for item in itens_unicos:
        f.write(f"{item}\n")

# Printar a lista no terminal
print("Lista única e ordenada:")
for item in itens_unicos:
    print(item)

print(f"Lista única e ordenada salva em {arquivo}.")
