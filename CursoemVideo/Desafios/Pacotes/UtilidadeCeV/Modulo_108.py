def aumentar(num, qtde=10):
    return num + ((num / 100) * qtde)


def diminuir(num, qtde=10):
    return num - ((num / 100) * qtde)


def dobro(num):
    return num * 2


def metade(num):
    return num / 2


def moeda(num):
    m = f'{num:_.2f}'
    return m.replace('.', ',').replace('_', '.')
