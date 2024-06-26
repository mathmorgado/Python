# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

#print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
#print(lista)

# Exatamente iguais!

lista = [numero * 2 for numero in range(10)] # List comprehension 

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto} # Esquerda do for é mapeamento!
    for produto in produtos
    if produto['preco'] > 10 # Direita do for é filtro!
]

print(*novos_produtos, sep='\n')

# lista = []
# for x in range(3):
#     for y in range(3):
#         print((x, y))
# print(f'List com 2 for: {lista}')

# lista = [(x, y) for x in range(3) for y in range(3)] -> list comprehension com 2 for

lista = [[(x, y) for y in range(3)] for x in range(3)]
print(f'List comprehension dentro de outra list comprehension: {lista}')