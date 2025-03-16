def ler_lista():
    lista = []
    while True:
        entrada = input("Digite um valor para a lista (ou #9 para finalizar): ")
        if entrada == "#9":
            break
        lista.append(entrada)
    return lista

print("Informe os valores da primeira lista:")
lista1 = ler_lista()

print("Informe os valores da segunda lista:")
lista2 = ler_lista()

if lista1 == lista2:
    print("As listas são iguais.")
else:
    print("As listas são diferentes.")
