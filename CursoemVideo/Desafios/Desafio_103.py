def ficha_jogador(nome='<desconhecido>', gol=0):
    return f'O jogador {nome} marcou {gol} gol(s) no campeonato!'


NomeJogador = str(input('Nome do jogador: ')).strip()
GolsMarcados = str(input('Quantidade de gols: ')).strip()

if NomeJogador == '' and GolsMarcados == '':
    print(ficha_jogador())

elif NomeJogador == '':
    print(ficha_jogador(gol=GolsMarcados))

elif GolsMarcados == '':
    print(ficha_jogador(NomeJogador))

else:
    print(ficha_jogador(NomeJogador, GolsMarcados))
