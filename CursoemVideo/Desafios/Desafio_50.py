list = []

for c in range(1, 7):
    num = int(input('Escolha um número: '))
    par = (num % 2)
    if par == 0:
        list.append(num)

print(f'A soma dos números pares escolhidos é: {sum(list)}')


m = 0
for c in range(1, 7):
    num = int(input('Escolha um número: '))
    if c % 2:
        m += c

print(f'A soma dos números pares escolhidos é: {sum(list)}')
