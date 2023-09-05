board = [
    [1, 2, 1],
    [2, 0, 1],
    [1, 2, 1],
]

hori_x = 0
vert_y = 0
found_zero = False

for i in range(len(board)):
    for j in board[i]:
        if j == 0:
            found_zero = True
        hori_x = j
        vert_y = j
