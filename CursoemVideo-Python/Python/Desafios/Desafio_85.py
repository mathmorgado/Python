lista = [[], []]

for i in range(1, 8):
    num = int(input(f'Digite o {i}º valor inteiro: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()

print(f'\nOs valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados forarm: {lista[1]}')
