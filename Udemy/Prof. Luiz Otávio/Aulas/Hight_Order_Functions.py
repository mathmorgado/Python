"""
Hight Order Functions ou Funções de Ordem superior, 
são funções que recebem outras funções como parâmentro e/ou
retornam uma outra função
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao,'Bom dia', 'Matheus')
)
