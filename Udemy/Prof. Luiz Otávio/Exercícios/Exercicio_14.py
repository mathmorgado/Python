from Exercicio_13_v2 import verificador_cpf 
import random

def gerador_cpf():
    cpf = ''

    for _ in range(0, 9):
        cpf += str(random.randint(0, 9))

    cpf += verificador_cpf(cpf, retornar_ultimos_digitos=True)
    return cpf


print(gerador_cpf())