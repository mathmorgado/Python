from random import randint
from time import sleep
jogos = list()
jogo = []

num_jogo = int(input('Quantos jogos você quer? '))

for c in range(1, num_jogo+1):
    for i in range(1, 7):
        jogo.append(randint(1, 61))
        if jogo[-1] in jogo[:-1] and i >= 2:
            jogo.pop()
            jogo.append(randint(1, 61))
    print(f'O {c}º jogo é: {jogo}')
    jogos.append(jogo[:])
    jogo.clear()
    sleep(0.75)
