def areas(Larg, Compri):
    area = Larg * Compri
    print(f'\nA área do terreno {largura:.2f} x {comprimento:.2f} é:'
          f' {area:.2f}m²')


print('\n    TERRENO')
print('-'*15)

largura = float(input('Largura(m): '))
comprimento = float(input('comprimento(m): '))
areas(largura, comprimento)
