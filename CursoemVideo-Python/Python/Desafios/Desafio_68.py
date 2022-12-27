import random

print('--- VAMOS JOGAR PAR OU ÍMPAR! ---')
resp = str(input('O que você quer? Par ou ímpar? '))
cont = 0

while True:
    num = int(input('Digite um número de 0 a 10: '))
    comp = random.randrange(0, 10)
    result = num + comp
    print(f'Eu escolhi {comp}. O valor final deu: {result}!')
    if result % 2 == 1 and resp.lower() == 'par':
        break
    elif result % 2 == 0 and resp.lower() == 'impar':
        break
    else:
        cont += 1
        print('Você ganhou! Vamos jogar denovo!')

print(f'Ufa! Ganhei depois de {cont} vitórias suas!')
