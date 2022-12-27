print('A seguir iremos realizar um PA (progressão aritmética). ')
pri_termo = int(input('Defina o 1º termo: '))
razao = int(input('Defina a razão: '))
lista = [pri_termo]

for c in range(1, 10):
    pa = lista[-1] + razao
    lista.append(pa)

print(f'Os 10 primeiros termos da progressão aritimética dada é: {lista}')
