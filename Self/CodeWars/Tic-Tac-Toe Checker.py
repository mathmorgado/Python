board = [
    [0, 0, 0],
    [1, 2, 2],
    [2, 0, 1],
]

hori_win = False
vert_win = False
diag_win = False
invert_diag_win = False

winner = None

found_zero = False
for i in range(len(board)):

    for h in range(len(board[i])):
        first_hori = [0][i]
        current_hori = board[i][h]

        if board[i][h] == 0:
            found_zero = True
            break

        if (current_hori != first_hori):
            hori_win = False
            break

        hori_win = True

    for v in range(len(board[i])):
        first_vert = [i][0]
        current_vert = board[v][i]

        if (current_vert != first_vert):
            vert_win = False
            break

        vert_win = True

    for d in range(len(board[i])):
        first_diag = board[0][0]
        current_diag = board[d][d]

        if (current_diag != first_diag):
            diag_win = False
            break

        diag_win = True

    for i_d in range(len(board[i])):
        invert_first = board[0][-1]
        invert_current_diag = board[d][-d]

        if (invert_current_diag != invert_first):
            invert_diag_win = False
            break

        invert_diag_win = True

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
        
        break

if hori_win or vert_win or diag_win or invert_diag_win:
    print(winner)
elif found_zero:
    print("Not finished")
else:
    print("Tie!")
