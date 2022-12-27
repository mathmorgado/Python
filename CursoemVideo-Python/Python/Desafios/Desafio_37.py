conversor = int(input('Para qual base numérica você deseja converter?'
                      '\n1-Binário.\n2-Octal.\n3-Hexadecimal.\n'
                      'Digite a opção desejada: '))

num = int(input('Digite o número decimal que deseja converter: '))

if conversor == 1:
    num = bin(num)
    print(f'O numero escolhido convertido para binário fica: {num[2:]}')

elif conversor == 2:
    num = oct(num)
    print(f'O numero escolhido convertido para octal fica: {num[2:]}')

elif conversor == 3:
    num = hex(num)
    print(f'O numero escolhido convertido para hexadecimal fica: {num[2:]}')

else:
    print('Opção inválida!')
