board = [
    [2, 1, 2],
    [2, 1, 1],
    [1, 1, 2],
]

hori_win = False
vert_win = False
diag_win = False
invert_diag_win = False

winner = None

found_zero = False

for i in range(len(board)):
    first_hori = board[i][0]
    first_vert = board[0][i]
    first_diag = board[0][0]
    invert_first = board[0][-1]

    current_hori = None
    current_vert = None
    current_diag = None
    invert_current_diag = None

    for h in range(len(board[i])):
        current_hori = board[i][h]

        if current_hori == 0:
            found_zero = True
            hori_win = False
            break

        if current_hori != first_hori:
            hori_win = False
            break

    for v in range(len(board[i])):
        current_vert = board[v][i]

        if current_vert == 0:
            found_zero = True
            vert_win = False
            break

        if current_vert != first_vert:
            vert_win = False
            break

    for d in range(len(board[i])):
        current_diag = board[d][d]

        if current_diag == 0:
            found_zero = True
            diag_win = False
            break

        if current_diag != first_diag:
            diag_win = False
            break

    for i_d in range(len(board[i])):
        invert_current_diag = board[i_d][-i_d]

        if invert_current_diag == 0:
            found_zero = True
            invert_diag_win = False
            break

        if invert_current_diag != invert_first:
            invert_diag_win = False
            break

    if hori_win or vert_win or diag_win or invert_diag_win:
        if hori_win:
            winner = first_hori
        elif vert_win:
            winner = first_vert
        elif diag_win:
            winner = first_diag
        else:
            winner = invert_first
        break

if hori_win or vert_win or diag_win or invert_diag_win:
    print(winner)
elif found_zero:
    print("Not finished")
else:
    print("Tie!")
