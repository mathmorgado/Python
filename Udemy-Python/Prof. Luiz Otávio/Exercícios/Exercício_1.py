while True:
    value = input('Digite um valor inteiro: ')

    if not value.isnumeric():
        print('ERROR: Por favor, digite um número inteiro!')

    else:
        if int(value) % 2 == 0:
            print('O valor digitado é PAR!')
        else:
            print('O valor digitado é ÍMPAR!')

        break
