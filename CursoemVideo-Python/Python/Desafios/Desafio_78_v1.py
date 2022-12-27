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

pos_maior = lista.index(maior)
pos_menor = lista.index(menor)

print(f'O menor valor é {menor} que está na {pos_menor + 1}º posição.')
print(f'\nO maior valor é {maior} que está na {pos_maior + 1}º posição.')
