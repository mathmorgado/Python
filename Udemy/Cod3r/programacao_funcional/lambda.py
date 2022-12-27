# Exemplo Procedural
a1 = [2, 3, 4]
a2 = []

for i in a1:
    a2.append(i * 2)

print(f'a1 - {a1}\na2 - lista:{a2}\na2 - Tupla:{tuple(a2)}')

# Funcional
compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14},
)

totais = tuple(
    map(
        lambda compra: compra['quantidade'] * compra['preco'], compras # funcao lambda ('fantasma')
    )
)

print(f'Preços totais: {totais}')
print(f'Total geral: {sum(totais)}')