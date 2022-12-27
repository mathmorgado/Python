#!/usr/local/bin/python3
from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    raio = sys.argv[1]
    area = circulo(raio)
    print(f'Area do circulo é: {area:.2f}')
    # sys.argv[] pega o indice da lista de argumentos do terminal. Ex:
    # Argv[0] = 'python ./ 1-Desafio_v7.py' and      Argv[1] = '12.4'
