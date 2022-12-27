def fatorial(valor, show=False):
    """
    -> Calcula o fatorial de um número
    :param valor: Numero a ser calculado
    :param show: Exibição do processo de calculo (Opcional)
    :return: Retorna o valor do fatorial/processo fatorial
    """
    f = 1
    if show is False:
        for c in range(valor, 0, -1):
            f *= c
        return f'{valor}! = {f}'
    else:
        print(f'{valor}! = ', end='')
        for c in range(valor, 1, -1):
            f *= c
            print(f'{c} x', end=' ')
        return print(f'1 = {f}')


valor = 7
print(fatorial(valor))
print(fatorial(valor, show=True))

help(fatorial)
