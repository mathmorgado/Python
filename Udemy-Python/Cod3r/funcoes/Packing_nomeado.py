# **kwargs = **kw -> parametros nomeados (dicionario), args -> argumentos
# *args = * -> parametros posicionais (list), args -> argumentos

# Pega os parametos nomeados e "empacota" em um dicionario, no caso o podium


def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')


if __name__ == '__main__':
    resultado_f1(primeiro='L. Hamilton',
                 segundo='M. Verstappen',
                 terceiro='S. Vettel')
