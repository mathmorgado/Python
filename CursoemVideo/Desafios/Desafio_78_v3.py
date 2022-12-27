lista = list()

menor = 0
maior = 0

for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    if c == 0:
        menor = lista[0]
        maior = lista[0]
    else:
        if menor >= lista[c]:
            menor = lista[c]
        if maior <= lista[c]:
            maior = lista[c]

print(f'O menor valor é {menor} que estão nas posições ', end='')

for i, v in enumerate(lista):
    if v == menor:
        print(f'|{i}| ', end='')

print(f'\nO maior valor é {maior} que estão nas posições ', end='')

for i, v in enumerate(lista):
    if v == maior:
        print(f'|{i}| ', end='')
