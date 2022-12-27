pessoas = {'nome': 'Matheus', 'sexo': 'm', 'idade': 16}

# Composição!
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print(f'\nO {pessoas["nome"]} tem {pessoas["idade"]} anos!\n')  # Aspas duplas

for k, v in pessoas.items():
    print(f'{k} = {v}\n')

del pessoas['sexo']
print(pessoas.items())

pessoas['peso'] = 58.5
print(pessoas.items())

Brazil = []
estado_1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado_2 = {'uf': 'São Paulo', 'sigla': 'SP'}

Brazil.append(estado_1)
Brazil.append(estado_2)

print(f'\n{Brazil}')
print(Brazil[1]['sigla'])
print(f'{Brazil[0]["uf"]}\n')  # Aspas duplas na aspas simples

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())

print('\n')

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
