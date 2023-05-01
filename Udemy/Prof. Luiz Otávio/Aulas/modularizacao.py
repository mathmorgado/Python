# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import importlib
import modularizacao_teste

print(f'Esse módulo se chama "{__name__}"\n')
print(modularizacao_teste.variavel)

for i in range(10):
    importlib.reload(modularizacao_teste)
    print(i)

print('Fim')