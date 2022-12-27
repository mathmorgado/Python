with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {} | Idade: {}'.format(*pessoa), file=saida)

    arquivo.close()

if arquivo.closed:
    print('O arquivo já foi fechado!')

if saida.closed:
    print('O arquivo de saída já foi fechado!')
