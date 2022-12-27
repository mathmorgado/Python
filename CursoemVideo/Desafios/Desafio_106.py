def titulo(txt):
    tamanho = (30 + len(txt))
    print('\33[96m~' * tamanho)
    print(' ' * 14, txt, ' ' * 14)
    print('~' * tamanho)


while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    resp = input('\33[39mFunção ou Biblioteca -> ')
    if resp.lower() == 'fim':
        break
    print('\33[93m')
    print(help(resp))
    print('\33[7; 92m ')

