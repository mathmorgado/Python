board = [
    [1, 1, 2],
    [1, 2, 1],
    [2, 1, 2],
]

found_zero = False

for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] != 0:
        print(f"O vencedor é o jogador {board[i][0]}")
        exit()

for i in range(3):
    if board[0][i] == board[1][i] == board[2][i] != 0:
        print(f"O vencedor é o jogador {board[0][i]}")
        exit()

if board[0][0] == board[1][1] == board[2][2] != 0:
    print(f"O vencedor é o jogador {board[0][0]}")
    exit()

if board[0][2] == board[1][1] == board[2][0] != 0:
    print(f"O vencedor é o jogador {board[0][2]}")
    exit()

for row in board:
    if 0 in row:
        found_zero = True

if found_zero:
    print("O jogo ainda não terminou")
else:
    print("O jogo empatou")
