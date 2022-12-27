total_gasto = 0
maior_mil = 0
cont = 0

while True:
    print('\n---CAIXA DE COMPRAS---')

    nome = str(input('Nome do produto: '))
    preco = float(input('Valor do produto: R$'))
    resp = str(input('Deseja continuar? '))

    if preco > 1000:
        maior_mil += 1

    if cont == 0:
        menor_preco = preco
        produto_barato = nome

    if preco < menor_preco:
        menor_preco = preco
        produto_barato = nome

    cont += 1
    total_gasto += preco

    if resp in 'Nnao':
        break

print(f'\nO total gasto na compra foi: R${total_gasto}')
print(f'Temos {maior_mil} produtos com valor maior que mil!')
print(f'O produto mais barato foi {produto_barato} à R${menor_preco}')
