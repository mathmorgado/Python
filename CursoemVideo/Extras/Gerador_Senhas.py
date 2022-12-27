import random

letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '123456789'
simbolos = '!@#$%&*?/'

use_for = letras_minusculas + letras_maiusculas + numeros + simbolos
tamanho_senha = 8

senha = ''.join(random.sample(use_for, tamanho_senha))

print(f'Sua senha é: {senha}')
