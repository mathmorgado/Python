# Laço de repetição

for c in range(0, 2):
    print('Goxtoso')
    print('Delícia')

# ir de 0 a 9
for c in range(0, 9):
    print(c)

# ir de 9 a 0
for c in range(9, 0, -1):
    print(c)

# ir de 0 a 9 pulando de 3 em 3
for c in range(0, 9, 3):
    print(c)

# Variavel para o laço
d = int(input('De: '))
a = int(input('Ate: '))
e = int(input('Em: '))

for c in range(d, a, e):
    print(c)
print('FIM')

# Variavel dentro do Laço
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os números escolhidos é: {s}')
