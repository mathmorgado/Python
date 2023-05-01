# import modulo_b -> Desse modo daria erro no main, pq o main tentaria importar esse módulo tmb, entretanto, do ponto de vista do main, esse módulo não existe pq ele está para trás da hierarquia das pastas.
from modularizacao_package.modulo_b import fala_oi

# "__all__" Seleciona o que será importado no "from nome_modulo import *" | '*' = all (tudo)
__all__ = [
    'variavel',
    'soma_do_modulo',
]

variavel = 'Alguma coisa\n'


def soma_do_modulo(x, y):
    return x + y


nova_variavel = 'Não é importada no __all__'
# fala_oi()