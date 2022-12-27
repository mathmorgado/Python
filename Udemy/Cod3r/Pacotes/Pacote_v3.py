# Resolver conflito de nome de modulos é simples! Dê um apelico usando "as" ou "import *"

from Pacote1 import modulo1 
from Pacote2 import modulo1 as mod
#from Pacote2.modulo1 import *

print('3 + 2 =', modulo1.soma(3, 2))
print('3 - 2 =', mod.subtracao(3, 2))
