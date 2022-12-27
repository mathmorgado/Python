print('~~~JOGO DA ADIVINHAÇÃO!~~~')
n = int(input('Tente adivinhar qual número estou pensando: '))
lista = [n]
c = 1


while n != 999:
    n = int(input('Errado! Tente novamente: '))
    c += 1
    lista.append(n)
    if c == 10:
        print('1º dica: Meu número tem 3 dígitos!')
    elif c == 15:
        print('2º dica: Meu número termina com 9!')
    elif c == 20:
        print('Ultima dica! Meu número também começa com 9!')

lista.remove(999)
print('\nParabéns, você acertou!')
print(f'\nTentativas: {c}\nNúmeros digitados: {lista}\nSoma: {sum(lista)}')
