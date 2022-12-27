#!/usr/local/bin/python3
from math import pi

print('Módulo: ', __name__)


def circulo(raio):
    print('A área do circulo é: ', pi * float(raio) ** 2)


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    circulo(raio)
