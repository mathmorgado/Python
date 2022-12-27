from random import randint
from time import sleep
jogadores = dict()
print('\nValores sorteados:')
for i in range(1, 5):
    dado = randint(1, 6)
    jogadores[i] = dado
    print(f'    O Jogador {i} tirou {dado}')
    sleep(0.75)
print('\nRanking dos Jogadores:')
for i in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'    O Jogador {i} tirou {jogadores[i]}')
    sleep(0.5)
