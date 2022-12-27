matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for L in range(0, 3):
    for c in range(0, 3):
        matriz[L][c] = int(input(f'Digite um valor para a posiçao {[L,c]}: '))

for L in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[L][c]:^5}]', end='')
