# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

# import importlib
# import modularizacao_teste# 
# import modularizacao_package.modulo
# from modularizacao_package.modulo import * # má prática
# from modularizacao_package import modulo


print(f'Esse módulo se chama "{__name__}"\n')
# print(modularizacao_teste.variavel)

# for i in range(10):
#     importlib.reload(modularizacao_teste)
#     print(i)

# print('Fim\n')

# print(*path, sep='\n')
# print(soma_do_modulo(1, 2))
# print(modularizacao_package.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel) -> Não é importada pelo __all__

# from modularizacao_package.modulo import fala_oi, soma_do_modulo

# print(__name__)
# fala_oi()

from modularizacao_package import fala_oi, soma_do_modulo # python acredita que o package "modularizacao_package" é um módulo!

print(soma_do_modulo(2, 3))
fala_oi()