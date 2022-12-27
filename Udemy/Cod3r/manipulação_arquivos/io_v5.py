with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {} | Idade: {}'.format(*registro.strip().split(',')))

    arquivo.close()

if arquivo.closed:
    print('O arquivo já foi fechado!')
