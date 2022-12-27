n = int(input('escolha um numero: '))
total = 0

for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[33m{c}', end=' ')
        total += 1
    else:
        print(f'\033[31m{c}', end=' ')
print(f'\n\033[mO número {n} foi divisível {total} vezes.')

if total <= 2:
    print(f'{n} é um número primo!')
else:
    print(f'{n} não é um número primo!')
