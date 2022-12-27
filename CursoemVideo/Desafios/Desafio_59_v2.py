val1 = int(input('Digite um valor inteiro: '))
val2 = int(input('Digite outro valor inteiro: '))
menu = 0

while menu != 5:
    menu = int(input('Escolha uma das opções abaixo:\n'
                     '[1]Somar\n[2]Multiplicar\n[3]Maior\n'
                     '[4]Novos valores\n[5]Sair do programa\n'))

    if menu == 1:
        print(f'{val1} + {val2} = {val1 + val2}')

    elif menu == 2:
        print(f'{val1} x {val2} = {val1 * val2}')

    elif menu == 3:
        if val1 < val2:
            print(f'{val2} é maior que o {val1}')
        elif val1 > val2:
            print(f'{val1} é maior que o {val2}')
        else:
            print('Ambos são iguais!')

    elif menu == 4:
        val1 = int(input('Digite um valor inteiro: '))
        val2 = int(input('Digite outro valor inteiro: '))

    elif menu == 5:
        exit()

    else:
        print('Opção inválida!')
