# Ajuste de Design
def titulo(txt):
    tamanho = (30 + len(txt))
    print('~' * tamanho)
    print(' ' * 14, txt, ' ' * 14)
    print('~' * tamanho)


def escreva(txt):
    print('-' * (4 + len(txt)))
    print(f'  {txt}  ')
    print('-' * (4 + len(txt)))


# Aula
titulo('DOCSTRING')
print('\n  Docstring é um documento/manual duma determinada função/built-in\n')

escreva('Usando: input.__doc__')
print(input.__doc__)
print('')

escreva('Usando: help(input)')
help(input)
print('')


escreva('Criando função com docstring')


def contador(i, f, p):  # Criando uma Docstring da minha função
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    print('-=' * 20)
    print(f'Contagem de {i} à {f} de {p} em {p}')
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')
    print('-=' * 20, '\n')


contador(2, 10, 2)

escreva('Docstring da função criada')
help(contador)  # Ver a docstring da minha função!

titulo('PARÂMETROS')
print('\n  Parâmentros é tudo aquilo que colocamos entre os () da função!\n')
escreva('Parâmentros posicionais, nomeados e opcionais')


def soma(a, b, c=0, d=0):
    """
    -> Faz a soma de pelo menos 2 valores e mostra o resultado.
    :param a: Primeiro valor (Obrigatório)
    :param b: Segundo valor  (Obrigatório)
    :param c: Terceiro valor (Opcional)
    :param d: Quarto valor   (Opcional)
    """
    sum = a + b + c + d
    return f'A soma vale: {sum}'


help(soma)

print('Como os parâmetros C e D são opcionais, não é necessário informalos:\n'
      f'\nsomar(2, 4):\n {soma(2, 4)}\n')  # Parâmetros posicionais (ordem)
print('E Com os parâmetros nomeado é possivel escolher qual parâmetro receberá'
      ' cada valor sem necessariamente seguir uma ordem específica:\n\nsomar'
      f'(b=3, a=2, d=4):\n {soma(b=3, a=2, d=4)}\n')  # Parâmetros nomeado

titulo('ESCOPOS')
print('\n  Escopo é o alcance de uma determinada variavel,'
      'sendo eles o Local e Global  \n')
escreva('Escopo Global x Local')
print('O Escopo Local é onde a variavel só existe dentro dum determinado '
      'local,\ncomo em uma função. Já o Global funciona em todo o programa!\n')


def teste_escopo(b):
    global d
    a = 8  # Escopo Local
    b += 4  # Escopo Local
    c = 2  # Escopo Local
    d = 8
    print('teste_escopo(b):')
    print(f'   A dentro vale {a}')
    print(f'   B dentro vale {b}')
    print(f'   C dentro vale {c}')
    print(f'   D dentro vale {d}')


a = 5  # Escopo Global
teste_escopo(a)
print(f'\nA fora vale {a}.')
print('Como B e C são do Escopo local, não existem fora da função!')
print('Já a variavel D, como foi usado o comando "global d",'
      f' fora também vale {d}.')

escreva('Return na função')
print('\n  Em uma função, o "return" realoca o valor dado aonde a função\
 for chamada, seja ela em uma variavel, em um print etc.  \n')


def fatorial(num=0):
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
    return fat


num = int(input('Número desejado à saber o fatorial: '))
print(f'{num}! = {fatorial(num)}')

fat1 = fatorial(5)
fat2 = fatorial(num)
fat_total = fat1 + fat2

print(f'A soma do fatorial de 5 e de {num} é: {fat_total}')
        