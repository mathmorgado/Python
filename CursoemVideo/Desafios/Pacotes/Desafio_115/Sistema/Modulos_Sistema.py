from time import sleep
from Pacotes.Desafio_115.Interface.Modulos_Interface import Menu, Titulo
from Pacotes.Desafio_115.Arquivo.Modulos_Arquivo import \
      LerArquivo, CadastroArquivo


def LeiaInt(entrada):
    while True:
        try:
            acesso = int(input(entrada))
        except (ValueError, TypeError):
            print('\033[31mERRO: Tipo de dado Inválido!'
                  ' Por favor, digite uma das opção válidas.')
            sleep(0.05)
            continue
        except KeyboardInterrupt:
            print('Usuário não escolheu nenhuma opção. Saindo do sistema!')
            acesso = 3
            return acesso
        else:
            return acesso


def Cadastros(entrada):
    while True:
        Menu('Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema')
        acesso = LeiaInt(entrada)

        if acesso == 1:
            LerArquivo('Pessoas.txt')

        elif acesso == 2:
            Titulo('NOVO CADASTRO')
            Nome = str(input('Nome: '))
            Idade = LeiaInt('Idade: ')
            CadastroArquivo('Pessoas.txt', Nome, Idade)

        elif acesso == 3:
            Titulo('SAINDO DO SISTEMA')
            exit()

        else:
            print('\033[31mERRO: Opção inválida! '
                  'Por favor, digite uma opção válida.\033[m')
            continue
