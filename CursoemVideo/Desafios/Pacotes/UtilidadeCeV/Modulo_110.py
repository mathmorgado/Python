def format(num):
    val = f'{num:_.2f}'
    val = val.replace('.', ',').replace('_', '.')
    return val


def resumo(num, aumento=10, redução=10):
    dobro = num * 2
    metade = num / 2
    aumento1 = num + (num/100 * aumento)
    redução1 = num - (num/100 * redução)
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \tR${format(num)}')
    print(f'Dobro do preço: \tR${format(dobro)}')
    print(f'Metade do preço: \tR${format(metade)}')
    print(f'{aumento}% de aumento: \tR${format(aumento1)}')
    print(f'{redução}% de redução: \tR${format(redução1)}')
    print('-' * 35)
