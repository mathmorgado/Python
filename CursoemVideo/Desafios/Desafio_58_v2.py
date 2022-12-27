from random import randint

print('----JOGO DA ADIVINHAÇÃO!----')
print('O computador irá escolher um número até 10. Você consegue adivinhar?')
print('\nHora de começar!\n')

comp_number = randint(0, 10)
acertou = False
erros = 1

while not acertou:
    player_number = int(input('Digite um número: '))
    if player_number == comp_number:
        acertou = True

    elif erros == 3:
        if player_number < comp_number:
            print('\nDica 1: O valor escolhido é menor! Tente outra vez.\n')
            erros += 1

    elif erros == 6:
        if player_number < comp_number:
            print('\nDica 2: O valor escolhido é menor! Tente outra vez.\n')
            erros += 1

        else:
            print('\nDica 2: O valor escolhido é maior! Tente outra vez.\n')
            erros += 1

    elif player_number != comp_number:
        print('Errado! Tente novamente.\n')
        erros += 1

print(f'Parabéns! Você acertou após {erros} tentativas!')
