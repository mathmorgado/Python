# Numeros entre 0 e 15
lista = [x for x in range(16)]
print(lista)

# Numeros par entre 0 e 30
lista = [x for x in range(31) if x % 2 == 0]
print(lista)

# Triplo de todo par entre 0 e 30
lista = [x * 3 for x in range(31) if x % 2 == 0]
print(lista)
