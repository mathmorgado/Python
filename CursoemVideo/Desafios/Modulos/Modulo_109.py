def aumentar(num, qtde=10, format=False):
    if format:
        val = num + ((num / 100) * qtde)
        val = f'{val:_.2f}'
        return val.replace('.', ',').replace('_', '.')
    else:
        return num + ((num / 100) * qtde)

def diminuir(num, qtde=10, format=False):
    if format:
        val = num - ((num / 100) * qtde)
        val = f'{val:_.2f}'
        return val.replace('.', ',').replace('_', '.')
    else:
        return num - ((num / 100) * qtde)


def dobro(num, format=False):
    if format:
        val = num * 2
        val = f'{val:_.2f}'
        return val.replace('.', ',').replace('_', '.')
    else:
        return num * 2


def metade(num, format=False):
    if format:
        val = num / 2
        val = f'{val:_.2f}'
        return val.replace('.', ',').replace('_', '.')
    else:
        return num / 2