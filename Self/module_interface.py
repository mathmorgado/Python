def linha(qted=45):
    print('\033[1m-\033[m' * qted)


def Titulo(msg):
    linha()
    print(f'{msg}'.center(45))
    linha()


def Menu(*Opções):
    Titulo('MENU PRINCIPAL')
    c = 1
    for opção in Opções:
        print(f'\033[93m{c}- \033[34m{opção}\033[m')
        c += 1
    linha()
