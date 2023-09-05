board = [
    [1, 2, 1],
    [2, 0, 1],
    [1, 2, 1],
]

hori_win = False
vert_win = False
diag_win = False

found_zero = False
for i in range(len(board)):

    for j in range(len(board[i])):
        current = board[i][j]

        hori_win = (board[i][j] == current)
        vert_win = (board[j][i] == current)

    diag_win = (board[i][i] == current)

if board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
    print("X win")
elif board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:
    print("O win")
elif found_zero:
    print("Not finished")
else:
    print("Tie!")
