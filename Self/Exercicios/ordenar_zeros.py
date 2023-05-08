def move_zeros(lst):
    return [x for x in lst if x] + [0]*lst.count(0)

print(move_zeros([0, 9, 0, 9, 1, 0, 0, 2, 1, 1, 3, 1, 9, 0, 0, 9]))