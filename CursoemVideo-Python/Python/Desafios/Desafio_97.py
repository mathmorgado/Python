def titulo(txt):
    tamanho = (16 + len(txt))
    print('-' * tamanho)
    print(' ' * 7, txt, ' ' * 7)
    print('-' * tamanho)


def escreva(txt):
    print('-' * (4 + len(txt)))
    print(f'  {txt}  ')
    print('-' * (4 + len(txt)))


titulo('TITULO')
escreva('CSV poura')
