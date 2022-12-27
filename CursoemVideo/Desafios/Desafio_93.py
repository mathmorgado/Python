gols = []
rendimento = {}
rendimento['nome'] = str(input('Nome: '))
rendimento['partidas'] = int(input('Partidas jogadas: '))

for c in range(1, rendimento['partidas'] + 1):
    gols.append(int(input(f'Qtde de gols na {c}º partida: ')))

rendimento['Gols/p'] = gols[:]
rendimento['Qtde_gols'] = sum(gols)

for k, v in rendimento.items():
    print(f'{k}: {v}')
