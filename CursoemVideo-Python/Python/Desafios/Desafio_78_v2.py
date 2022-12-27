lista = list()

for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))

lista.sort(reverse=True)

for c, v in enumerate(lista):
    if c == 0:
        print(f'\nO maior valor é {v} que está na {c + 1}º posição')
    if c == 4:
        print(f'O menor valor é {v} que está na {c + 1}º posição')
