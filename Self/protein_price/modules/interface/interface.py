def line(qty=45):
    print('\033[1m-\033[m' * qty)


def title(msg):
    line()
    print(f'{msg}'.center(45))
    line()


def menu(*Options):
    title('MENU')
    c = 1
    for option in Options:
        print(f'\033[93m{c}- \033[34m{option}\033[m')
        c += 1
    line()
