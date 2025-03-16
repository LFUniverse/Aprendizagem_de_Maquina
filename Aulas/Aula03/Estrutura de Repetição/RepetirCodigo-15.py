# Cria números randômicos (aleatórios)
import random

# Cria uma lista com 10 números aleatórios entre 1 e 100
lstNumeros = [random.randint(1, 100) for _ in range(10)]

# Cria uma lista de 10 números distintos entre 1 e 100
lstUnica = random.sample(range(1, 101), 10)

print (len(lstUnica))
print (lstUnica)