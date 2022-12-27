num = int(input('Digite um número inteiro: '))
num1 = num
fatorial = 1

print(f'{num1}! = ', end='')

while num > 0:
    print(f'{num}', end='')
    print(' x ' if num > 1 else ' = ', end='')
    fatorial *= num
    num -= 1

print(f'{fatorial}')
