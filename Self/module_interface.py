def linha(qted=45):
    print('\033[1m-\033[m' * qted)


def Titulo(msg):
    linha()
    print(f'\033[93m{msg:^45}\033[m')
    linha()


def Menu(*Opções, title):
    Titulo(title)
    c = 1
    for opção in Opções:
        print(f'{c}- {opção}\033[m')
        c += 1
    print()
