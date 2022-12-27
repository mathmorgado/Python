from random import randint
numeros = []


def sorteio():
    while len(numeros) != 5:
        for _ in range(0, 5):
            n = randint(0, 101)
            if n not in numeros:
                numeros.append(n)
    return numeros


def SomaPar():
    SumPar = 0
    for value in numeros:
        if value % 2 == 0:
            SumPar += value
    return SumPar


print(f'Sorteando 5 números: {sorteio()}')
print(f'A soma entre os pares é: {SomaPar()}')
