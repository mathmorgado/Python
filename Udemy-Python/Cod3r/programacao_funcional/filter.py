pessoas = [ 
    {'nome': 'Pedro', 'idade': 17},
    {'nome': 'Raphaell', 'idade': 10},
    {'nome': 'Alex', 'idade': 43},
    {'nome': 'Andreia', 'idade': 37},
    {'nome': 'Gabriel', 'idade': 6},
    {'nome': 'Viana', 'idade': 26}
]

menores = filter(lambda pessoa: pessoa['idade'] < 18, pessoas)

nome_grande = filter(lambda pessoa: len(pessoa['nome']) > 6, pessoas)

print(list(nome_grande))