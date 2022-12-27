with open('desafio-ibge.csv', 'r') as arq:
    for linha in arq:
        c = linha.strip().split(',')
        print('{}: {}'.format(*c[8:9], *c[3:4]))
