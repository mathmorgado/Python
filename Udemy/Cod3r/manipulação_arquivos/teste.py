with open('teste.csv', 'r') as arq:
    for linha in arq:
        c = linha.strip().split(',')
        print('arg 1: {} | arg 2: {}'.format(*c[:1], *c[2:3]))
