pessoas = []
cadastro = {}
idades = []
mulheres = []
idade_acima = []

while True:
    cadastro['Nome'] = str(input('Nome: '))
    cadastro['Idade'] = int(input('Idade: '))
    cadastro['Sexo'] = str(input('Sexo[M/F]: '))
    while cadastro['Sexo'] not in 'MmFf':
        cadastro['Sexo'] = str(input('Erro! Sexo[M/F]: '))
    pessoas.append(cadastro.copy())

    resp = str(input('Deseja continuar[S/N]? '))

    while resp not in 'SsNn':
        resp = str(input('Erro! Deseja continuar[S/N]? '))

    if resp in 'Nn':
        break

for c in range(0, len(pessoas)):
    idades.append(pessoas[c]['Idade'])

media = sum(idades) / len(idades)

for c in range(0, len(pessoas)):
    if pessoas[c]['Idade'] > media:
        idade_acima.append(pessoas[c])

for c in range(0, len(pessoas)):
    if pessoas[c]['Sexo'] in 'Ff':
        mulheres.append(pessoas[c])

print('\n--INFORMAÇÕES--')
print(f'-Foram cadastradas {len(pessoas)} pessoas.')
print(f'-A média da idade das pessoas cadastradas é: {media:.2f}')
print('-Lista com as mulheres: ', end='')
for c in range(0, len(mulheres)):
    print(f'|{mulheres[c]["Nome"]}', end='| ')
print('\n-Pessoas com idade acima da média: ', end='')
for c in range(0, len(idade_acima)):
    print(f'|{idade_acima[c]["Nome"]}', end='| ')
