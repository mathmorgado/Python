secret_word = 'frango empanado'
wrong_letters = ''
secret_letters = ''
word = ''

print('TEMA: Comida\n')

while word != secret_word:
    word = ''

    for letter in secret_word:
        if letter != ' ':
            word += letter if letter in secret_letters else '*'
        else:
            word += ' '

    print(word, f'\n\nErradas: {wrong_letters}\n')

    guess = input('Digite uma letra: ')

    if guess in secret_word:
        secret_letters += guess
    else:
        wrong_letters += guess
