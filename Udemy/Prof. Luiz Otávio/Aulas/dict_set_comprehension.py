# Dictionary Comprehension e Set comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'escritório'
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor # mapeamento
    for chave, valor in produto.items()
    if chave != 'categoria' # filtro
}

print(dc)

s1 = {2 ** i for i in range(10)}
print(s1)