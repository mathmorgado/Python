def move_zeros(lst):
    qtde_zeros = lst.count(0)

    while lst[-qtde_zeros:] != [0] * qtde_zeros:
        for i in range(len(lst)):
            if lst[i] == 0:
                lst.pop(i)
                lst.append(0)
    return qtde_zeros

print(move_zeros([0, 9, 0, 9, 1, 0, 0, 2, 1, 1, 3, 1, 9, 0, 0, 9]))