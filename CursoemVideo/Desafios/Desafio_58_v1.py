from random import randint

print('----JOGO DA ADIVINHAÇÃO!----')
print('O computador irá escolher um número até 10. Você consegue adivinhar?')
print('\nHora de começar!\n')

comp_number = randint(0, 10)
player_number = int(input('Digite um número: '))
erros = 1

while player_number != comp_number:
    print('Nananinanão!')
    erros += 1
    player_number = int(input('Digite outro número: '))

print(f'Parabéns! Você acertou após {erros} tentativas!')
