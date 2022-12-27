#!/usr/local/bin/python3

from math import pi

if __name__ == '__main__':

    raio = float(input('Qual o raio da circunferencia? '))

    Area = pi * raio ** 2

    print(f'A área da circunferencia é: {Area:.2f}')
