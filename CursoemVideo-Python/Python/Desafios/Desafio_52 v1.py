num = int(input('Escolha um número inteiro aleatório: '))

if num == 2 or num == 5 or num == 7 or num == 11:
    print('O número escolhido é primo!')

else:
    for c in range(0, 1):
        valor = num % 2
        if valor == 0:
            continue
        valor = num % 5
        if valor == 0:
            continue
        valor = num % 7
        if valor == 0:
            continue
        valor = num % 11
        if valor == 0:
            print('O numero escolhido não é primo!')
        else:
            print('O número escolhido é primo!')
