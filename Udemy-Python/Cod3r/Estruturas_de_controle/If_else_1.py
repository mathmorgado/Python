pontuação = float(input('Qual a pontuação do aluno? '))


class TermCol:
    AZUL = '\033[34m'
    VERMELHO = '\033[91m'
    NORMAL = '\033[0m'


def nota_azul(valor, valor_2, nota):
    if pontuação >= valor and pontuação <= valor_2:
        print(f'Você recebeu um {TermCol.AZUL}{nota}{TermCol.NORMAL} !')


def nota_vermelha(valor, valor_2, nota):
    if pontuação >= valor and pontuação <= valor_2:
        print(f'Você recebeu um {TermCol.VERMELHO}{nota}{TermCol.NORMAL}!')


if pontuação > 10:
    print(TermCol.VERMELHO +
          'NOTA INVÁLIDA: A pontuação deve ser menor que 10!' +
          TermCol.NORMAL)

nota_azul(9.1, 10, 'A')
nota_azul(8.1, 9, 'A-')
nota_azul(7.1, 8, 'B')
nota_azul(6.1, 7, 'B-')
nota_vermelha(5.1, 6, 'C')
nota_vermelha(4.1, 5, 'C-')
nota_vermelha(3.1, 4, 'D')
nota_vermelha(2.1, 3, 'D-')
nota_vermelha(1.1, 2, 'E')
nota_vermelha(0.0, 1, 'E-')

if pontuação < 0:
    print(TermCol.VERMELHO +
          'NOTA INVÁLIDA: A pontuação deve ser maior que 0!' +
          TermCol.NORMAL)
