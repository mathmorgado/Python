from Pacotes.Desafio_115.Interface.Modulos_Interface import Titulo, linha


def ArquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CriarArquivo(arq):
    try:
        arquivo = open(arq, 'wt+')
        arquivo.close()
    except Exception:
        print('\033[31mERRO: Arquivo não pôde ser criado!\033[m')


def LerArquivo(arq):
    try:
        arquivo = open(arq, 'rt')
    except FileNotFoundError:
        print('\033[31mERRO: Arquivo não pôde ser lido!\033[m')
    else:
        Titulo('PESSOAS CADASTRADAS')
        for registro in arquivo:
            pessoa = registro.strip().split(';')
            pessoa[1] = pessoa[1].replace('\n', '')
            print(f'{pessoa[0]:<30} {pessoa[1]:>3} anos')
        linha()
    finally:
        arquivo.close()


def CadastroArquivo(arq, nome, idade):
    try:
        arquivo = open(arq, 'at')
    except Exception:
        print('Erro ao abrir!')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except Exception:
            print('Erro ao escrever!')
        else:
            print(f'Registro de \033[1m{nome}\033[m feito com sucesso!')
            linha()
    finally:
        arquivo.close()
