#!/usr/local/bin/python3
from math import pi

print('Módulo: ', __name__)


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area = circulo(raio)
    print(f'Area do circulo é: {area:.2f}')
