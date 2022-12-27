def fatorial(valor, show=False):
    """
    -> Calcula o fatorial de um número
    :param valor: Numero a ser calculado
    :param show: Exibição do processo de calculo (Opcional)
    :return: Retorna o valor do fatorial/processo fatorial
    """
    f = 1
    for c in range(valor, 0, -1):
        if show:
            print(c, end='') 
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


valor = 5
print(fatorial(valor, show=True))
help(fatorial)
