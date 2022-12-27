print('A seguir, iremos descobrir se a frase/palavra é um palindromo!\n'
      'Exemplo de palindromo: osso, radar, ovo')

resp = str(input('Digite uma frase ou uma palavra: ')).replace(' ', '')

if resp[:].lower() == resp[::-1].lower():
    print('A frase/palavra é um palíndromo!')
else:
    print('A frase/palavra não é um palíndromo!')
