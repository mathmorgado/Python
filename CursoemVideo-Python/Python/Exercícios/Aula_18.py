pessoas = [['Matheus', 21], ['Ana', 22], ['Pedro', 17], ['Maria', 45]]

print(pessoas[1][0])

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade!\n')

pessoas = list()
dados = list()

for c in range(0, 3):
    print(30*'-', end='')
    dados.append(str(input('\nDigite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    pessoas.append(dados[:])
    dados.clear()

# Limpar a list dados permite "formar outras listas"

print(pessoas)
totmai = 0
totmen = 0

for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores de idade e {totmen} menores de idade.')
