lista = []

while True:
    num = int(input('\nDigite um valor: '))
    resp = str(input('Deseja continuar: '))
    lista.append(num)
    if resp in 'NnÂaAaoo':
        break

print(f'\nForam digitados {len(lista)} números!')

lista.sort(reverse=True)

print(f'A ordem decrescente dos números é: {lista}')

if 5 in lista:
    print('5 foi digitado e está na lista!')
else:
    print('5 não foi digitado, logo não está na lista')
