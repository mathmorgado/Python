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
    print(' ' * 9, 'RESUMO DO VALOR', ' ' * 9)
    print('-' * 35)
    print(f'Preço analisado:     R${format(num)}')
    print(f'Dobro do preço:      R${format(dobro)}')
    print(f'Metade do preço:     R${format(metade)}')
    print(f'{aumento}% de aumento:      R${format(aumento1)}')
    print(f'{redução}% de redução:      R${format(redução1)}')
    print('-' * 35)
