"""Calculadora com while"""

while True:
    # input dados
    num_1 = input('Digite um valor: ')
    num_2 = input('Digite outro valor: ')
    operador = input('Digite um operador: ')

    # validação dos dados
    num_1_float = 0
    num_2_float = 0
    numeros_validos = None

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('\n\033[31mValores inválidos!\033[m\n')
        continue

    if operador not in '+-/*':
        print('\n\033[31mOperador inválido!\033[m\n')
        continue

    # conta
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = {num_1_float + num_2_float}')
    
    if operador == '-':
        print(f'{num_1_float} - {num_2_float} = {num_1_float - num_2_float}')
    
    if operador == '*':
        print(f'{num_1_float} * {num_2_float} = {num_1_float * num_2_float}')

    if operador == '/':
        print(f'{num_1_float} / {num_2_float} = {num_1_float / num_2_float}')

    # break
    sair = input('Deseja sair [s]: ').lower().startswith('s')

    if sair:
        break