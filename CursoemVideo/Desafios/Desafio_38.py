numero1 = int(input('Digite um número inteiro qualquer: '))
numero2 = int(input('Digite outro número inteiro qualquer: '))

if numero1 > numero2:
    print(f'{numero1} é maior que {numero2}.')
elif numero1 == numero2:
    print('Ambos tem o mesmo valor.')
else:
    print(f'{numero2} é maior que {numero1}.')

if numero1 % 2 != 0 and numero2 % 2 != 0:
    print('Ambos são ímpares!')
elif numero1 % 2 == 0 and numero2 % 2 == 0:
    print('Ambos são pares!')
else:
    if numero1 % 2 != 0:
        print(f'{numero1} é ímpar!')
    else:
        print(f'{numero1} é par!')

    if numero2 % 2 != 0:
        print(f'{numero2} é ímpar!')
    else:
        print(f'{numero2} é par!')
