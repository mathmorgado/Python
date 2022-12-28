from functools import reduce

pessoas = [ 
    {'nome': 'Pedro', 'idade': 17},
    {'nome': 'Raphaell', 'idade': 10},
    {'nome': 'Alex', 'idade': 43},
    {'nome': 'Andreia', 'idade': 37},
    {'nome': 'Gabriel', 'idade': 6},
    {'nome': 'Viana', 'idade': 26}
]
menor_idade = list(filter(lambda p: p['idade'] < 18, pessoas ))

idades = list(map(lambda x: x['idade'], menor_idade))

sum_idade = reduce(lambda idades, idade: idades + idade, idades, 0)
print(sum_idade)
