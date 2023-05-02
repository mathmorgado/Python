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

def zipper(lista_1, lista_2):
    tamanho_lista_1 = len(lista_1)
    tamanho_lista_2 = len(lista_2)
    uniao_listas = []

    if tamanho_lista_1 < tamanho_lista_2:
        menor_lista = lista_1
        maior_lista = lista_2
        i = range(0, len(maior_lista))
    else:
        menor_lista = lista_2
        maior_lista - lista_1
        i = range(0, len(maior_lista))

    for item in menor_lista:
        uniao = (item, maior_lista[i])
        uniao_listas.append(uniao)
        i += 1

    return uniao_listas


lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(lista_1, lista_2))

