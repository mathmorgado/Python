# Inverter uma lista sem usar slices! -> [::-1]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pos_final  = len(lista) - 1

for i in range(len(lista)//2):
    pos_inicial = lista[i]

    lista[i] = lista[pos_final]
    lista[pos_final] = pos_inicial

    pos_final -= 1

print(lista)

"""
Esse método não tem a necessidade de criar uma 2º lista,
ocupando menos espaço na memória. Além disso, não é neces-
sário percorrer toda a lista, apenas metade dela!
"""
