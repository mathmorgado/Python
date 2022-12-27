num = [2, 4, 9, 1]
print(f'1º Lista - {num}')

num[2] = 3
print(f'2º Lista - {num}')

num.append(7)
print(f'3º Lista - {num}')

num.sort(reverse=True)
print(f'4º Lista - {num}')

# Insere um elemento após a chave informada
num.insert(2, 0)
print(f'5º Lista - {num}')

# Remove o último valor/a chave informada
num.pop()
print(f'6º Lista - {num}')

if 5 in num:
    num.remove(5)
    print(num)
else:
    print('\nNão achei o valor 5!\n')


# "Embelezar" a lista.
for v in num:
    print(f'|{v}|\n', end='')

# Colocar valores input na lista!
val = list()
for cont in range(0, 5):
    val.append(int(input('Digite um valor: ')))

# Organizar a lista
for c, v in enumerate(val):
    print(f'Na posição {c}, achei o valor {v}!')
print('Fim!')

print(f'\nEssa lista tem {len(val)} elementos.\n')

# Ligação entre duas listas(alterou uma, altera as duas)!

print('Conectando as listas')

num = val
print(f'Lista 1: {num}\nLista 2: {val}\n')

print('Alterando o valor de uma:\n')

num[2] = 12
print(f'Lista 1: {num}\nLista 2: {val}\n')

# Uma lista recebe os valores da outra.

print('Igualando as listas')

num = val[:]
print(f'Lista 1: {num}\nLista 2: {val}\n')

print('Alterando o valor de uma:\n')

num[2] = 8
print(f'Lista 1: {num}\nLista 2: {val}\n')
