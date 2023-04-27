
# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        item.add(44)
        print(f'\nSET\n{item}')

    elif isinstance(item, str):
        print(f'\nSTR\n{item.upper()}')

    elif isinstance(item, (int, float)):
        print(f'\nNUM\n{item} x 2 = {item*2}')

    else:
        print(f'\nOUTRO\n{item}')