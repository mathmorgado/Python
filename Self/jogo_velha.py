wrong_letters = ''
secret_word = 'frango empanado'
secret_letters = ''
word = ''


print(word, '\nTEMA: Comida')

while word != secret_word:
    word = ''
    guess = input('Digite uma letra: ')

    if guess in secret_word:
        secret_letters += guess
    else:
        wrong_letters += guess

    for letter in secret_word:
        if letter != ' ':
            word += letter if letter in secret_letters else '*'
        else:
            word += ' '

    print(word, f'{wrong_letters}')
