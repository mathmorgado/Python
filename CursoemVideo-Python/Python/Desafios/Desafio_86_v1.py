matriz = []

list1 = []
list2 = []
list3 = []


for v in range(0, 3):
    list1.append(int(input(f'Digite um valor para posição [{0}, {v}]: ')))
    list2.append(int(input(f'Digite um valor para posição [{1}, {v}]: ')))
    list3.append(int(input(f'Digite um valor para posição [{2}, {v}]: ')))

matriz.append(list1)
matriz.append(list2)
matriz.append(list3)

print('\n', 30*'-')

print(matriz[0], end='\n')
print(matriz[1], end='\n')
print(matriz[2], end='\n')
