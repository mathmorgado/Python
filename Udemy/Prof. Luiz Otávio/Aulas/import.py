# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import "nome_modulo"
# Vantagens: você tem o namespace do módulo e sem risco de sobrescrever uma variavel ou função
# Desvantagens: nomes grandes
import sys

platform = 'A MINHA'
print(f'Variavel "platform" da biblioteca sys: ', sys.platform)
print(f'Minha variavel "platform": {platform}\n')

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: chamadas menores e atende a necessidade mais específicamente
# Desvantagens: Sem o namespace do módulo, risco de sobrescrever a variavel ou função
from sys import exit, platform

platform = 'Variavel platform do sys'
print('Variavel "platform" do sys, agora sobrescrita: ', platform)

# import nome_modulo as apelido
import math as mt

math = '\nnome do modulo sem sobrescrevelo'
print(math)
print(mt.pi)


# from nome_modulo import objeto as apelido
from sys import exit as ex
from sys import platform as pf

print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: torna o código ilegivel e traz muitas funções/ variaveis implicitamente.
# from sys import exit, platform

# print(platform)
# exit()