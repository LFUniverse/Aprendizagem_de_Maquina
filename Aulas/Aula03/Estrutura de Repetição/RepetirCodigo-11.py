lista1 = [1, 2, 3]

lista2 = ['a', 'b', 'c']

resultado = zip(lista1, lista2)

for x,y in resultado:
    print(f'Primeiro elemento: {x} e segundo: {y}')

# resultado = [(1,”a”),(2,”b”),(3,”c”)]

# saída:

# Primeiro elemento: 1 e segundo: a
# Primeiro elemento: 2 e segundo: b
# Primeiro elemento: 3 e segundo: c