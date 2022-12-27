print('A seguir iremos realizar um PA (progressão aritmética). ')
pri_termo = int(input('Defina o 1º termo: '))
razao = int(input('Defina a razão: '))
pa = pri_termo
c = 1

while c != 11:
    print(pa, end=' ')
    pa += razao
    c += 1

print('\ncabo!')
