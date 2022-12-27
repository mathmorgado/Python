jogador = []
gols = []
rendimento = {}

while True:
    rendimento['Nome'] = str(input('Nome: '))
    Partidas = int(input('Partidas jogadas: '))

    for c in range(1, Partidas + 1):
        gols.append(int(input(f'Total de gols na {c}º partida: ')))
    rendimento['Gols'] = gols.copy()
    rendimento['Total'] = sum(gols)
    gols.clear()
    jogador.append(rendimento.copy())
    resp = str(input('Deseja continuar[S/N]? '))
    if resp in 'Nn':
        break

print('\n', 39 * '-')
print('Cod Nome', 10 * ' ', 'Goals', 7 * ' ', 'Total')
print(40 * '-')

for i in range(0, len(jogador)):
    print(f'{i}', end='   ')
    for v in jogador[i].values():
        print(f'{v}', (15 - len(str(v))) * (' '), end=(''))
    print('')

codigo = int(input('\n- Levantamento - Código do jogador:[exit -> 999] '))
while codigo != 999:
    for i in range(1, len(jogador[codigo]['Gols']) + 1):
        print(f'   No {i}º jogo fez {jogador[codigo]["Gols"][i - 1]} gols')
