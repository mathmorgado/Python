board = [
    [1, 2, 1],
    [2, 1, 2],
    [1, 0, 1],
]

hori_win = False
vert_win = False
diag_win = False

winner = None

found_zero = False
for i in range(len(board)):
    first = board[i][0]

    for h in range(len(board[i])):
        current_hori = board[i][h]

        if board[i][h] == 0:
            found_zero = True

        if (current_hori != first):
            hori_win = False
            break

        hori_win = True

    for v in range(len(board[i])):
        current_vert = board[v][i]

        if (current_vert != first):
            vert_win = False
            break

        vert_win = True

    for d in range(len(board[i])):
        invert_first = board[-1][-1]

        current_diag = board[d][d]
        invert_current_diag = board[-d][-d]

        if (current_diag != first or invert_current_diag != invert_first):
            diag_win = False
            break

        diag_win = True

    if hori_win or vert_win or diag_win:
        winner = first
        break

if hori_win or vert_win:
    print(winner)
elif found_zero:
    print("Not finished")
else:
    print("Tie!")
