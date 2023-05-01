"""
Exercícios
1- Aumente os preços dos produtos a seguir em 10%
Gere novos_produtos por deep copy (cópia profunda)

2- Ordene os produtos por nome decrescente (do maior para menor)
Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

3- Ordene os produtos por preco crescente (do menor para maior)
Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
"""
from copy import deepcopy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


# Primeiro Exercício

novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in produtos.copy()
]
#print(novos_produtos)

# Segundo Exercício

produtos_ordenados_por_nome = sorted( 
    deepcopy(novos_produtos),
    key=lambda produto: produto['nome'],
    reverse=True
)

print(*produtos_ordenados_por_nome, sep='\n', end='\n\n')

# Terceiro Exercício

produtos_ordenados_por_preco = sorted(
    deepcopy(novos_produtos),
    key=lambda produto: produto['preco']
)

print(*produtos_ordenados_por_preco, sep='\n', end='\n\n')
