matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = []

for L in range(0, 3):
    for c in range(0, 3):
        matriz[L][c] = int(input(f'Digite um valor para a posição[{[L,c]}]: '))

coluna_3 = 0

for L in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[L][c]:^5}]', end='')
        if matriz[L][c] % 2 == 0:
            par.append(matriz[L][c])
    print()
    coluna_3 += matriz[L][2]
    if matriz[1][c] > matriz[1][c-1]:
        if matriz[1][c] > matriz[1][c-2]:
            maior = matriz[1][c]
        else:
            matriz[1][c-2]
            maior = matriz[1][c-2]
    else:
        maior = matriz[1][c-1]

print('\n', 15*'-=')

print(f'A soma dos números pares é: {sum(par)}')
print(f'A soma dos números da 3º coluna é: {coluna_3}')
print(f'O maior número da linha dois é: {maior}')
