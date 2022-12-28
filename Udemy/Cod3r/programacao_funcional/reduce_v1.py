from functools import reduce

pessoas = [ 
    {'nome': 'Pedro', 'idade': 17},
    {'nome': 'Raphaell', 'idade': 10},
    {'nome': 'Alex', 'idade': 43},
    {'nome': 'Andreia', 'idade': 37},
    {'nome': 'Gabriel', 'idade': 6},
    {'nome': 'Viana', 'idade': 26}
]

# Função redunce recebe um lambdad com 2 parâmentros: Um acumulador e um 'lista'. 
sum_idade = reduce(lambda idades, p: idades + p['idade'], pessoas, 0) # Depois de definir o lambda, se passa a lista e onde o acumulador starta
print(sum_idade)