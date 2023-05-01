# "__all__" Seleciona o que será importado no "from nome_modulo import *" | '*' = all (tudo)
__all__ = [
    'variavel',
    'soma_do_modulo',
]

variavel = 'Alguma coisa'


def soma_do_modulo(x, y):
    return x + y


nova_variavel = 'Não é importada no __all__'