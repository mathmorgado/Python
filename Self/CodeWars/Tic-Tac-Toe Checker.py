board = [
    [1, 2, 1],
    [2, 0, 1],
    [1, 2, 1],
]

hori_win = True
vert_win = True
diag_win = True

stop_hori = False
stop_vert = False

winner = None

found_zero = False
for i in range(len(board)):
    first = board[i][0]

    for j in range(len(board[i])):
        current_hori = board[i][j]
        current_vert = board[j][i]

        if board[i][j] == 0:
            found_zero = True

        if (current_hori != first or stop_hori):
            hori_win = False
            stop_hori = True

        if (current_vert != first or stop_vert):
            vert_win = False
            stop_vert = True

    if hori_win or vert_win:
        winner = first
        break

    diag_win = (board[i][i] == first)

if hori_win or vert_win or diag_win:
    print(winner)
elif found_zero:
    print("Not finished")
else:
    print("Tie!")
