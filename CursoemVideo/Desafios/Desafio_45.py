import random

jogo = input('Vamos jogar jokenpo? '
             '\nSim'
             '\nNão'
             '\nResposta: ')

while jogo == 1 or jogo.lower() == 'sim':
    lista = ['pedra', 'papel', 'tesoura']
    oponente = lista[random.randint(0, len(lista) - 1)]
    resposta = input('Pedra, papel ou tesoura? ').strip()

    print(f'O computador escolheu: {oponente}!')

    if resposta == oponente:
        print('Empate!')

    if resposta == 'pedra' and oponente == 'tesoura':
        print('Você venceu!')
    elif resposta == 'pedra' and oponente == 'papel':
        print('Você perdeu!')

    if resposta == 'tesoura' and oponente == 'papel':
        print('Você venceu!')
    elif resposta == 'tesoura' and oponente == 'pedra':
        print('Você perdeu!')

    if resposta == 'papel' and oponente == 'pedra':
        print('Você venceu!')
    elif resposta == 'papel' and oponente == 'tesoura':
        print('Você perdeu!')

    jogo = input('Deseja continuar? '
                 '\nSim'
                 '\nNão'
                 '\nResposta: ')
    continue

print('Obrigado pelo jogo!')
