print('-= JOGO DA FORCA =-')

palavra_secreta = 'cheirosa'
digitado = []
CHANCES = 5


while True:
    if CHANCES <= 0:
        print(f'Você perdeu!')
    
    letra = input('\nDigite uma única letra: ').lower()

    if len(letra) > 1:
        print('ERROR: Por favor, digite apenas uma letra!')
        continue

    digitado.append(letra)

    if letra in palavra_secreta:
        print('\nParabéns, você acertou uma letra!')
    else:
        print('\nQue pena, essa letra não faz parte da palavra secreta.')
        digitado.pop()
    
    secreto_temporario = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in digitado:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    
    print(secreto_temporario)

    if secreto_temporario == palavra_secreta:
        print('\nParabéns, você descobriu a palavra secreta!')
        break

    if letra not in palavra_secreta:
        CHANCES -= 1
    
    print(f'Você ainda tem {CHANCES} chances!')
