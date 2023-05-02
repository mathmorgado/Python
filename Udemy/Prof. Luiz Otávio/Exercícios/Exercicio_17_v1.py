# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# from itertools import zip_longest
def zipper(lista_1, lista_2):
    intervalo_maximo = min(len(lista_1), len(lista_2)) # Vai retornar o ultimo indice da menor lista!
    return [(lista_1[i], lista_2[i]) for i in range(intervalo_maximo)]


lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(lista_1, lista_2))
# print(list(zip(lista_1, lista_2)))
# print(list(zip_longest(lista_1, lista_2))) -> Ordem apartir da maior lista!