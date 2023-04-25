nome = input('Primeiro nome: ')

if len(nome) <= 4:
    print('Seu nome é pequeno!')

if len(nome) > 4 and len(nome) <= 6:
    print('Seu nome é normal!')

if len(nome) > 6:
    print('Seu nome é Gigante!')

