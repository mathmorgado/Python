"""
Resolver conflito de nome de modulos é simples!
Dê um apelido usando 'as'. Ex: import pandas as pd
"""

from Pacote1 import modulo1
from Pacote2 import modulo1 as mod
# from Pacote2.modulo1 import *

print('3 + 2 =', modulo1.soma(3, 2))
print('3 - 2 =', mod.subtracao(3, 2))
