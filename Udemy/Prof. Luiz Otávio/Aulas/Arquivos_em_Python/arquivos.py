# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

# caminho_arquivo = 'C:\\Users\\Matheus\\OneDrive\\Documentos importantes\\Documentos\\Estudos Programação\\Python\\Udemy\\Prof. Luiz Otávio\\Aulas\\Arquivos_em_Python\\aula116.txt' -> Sempre que o caminho precisar usar '\', ao invés de 1 use 2 \\

caminho_arquivo = 'aula116.txt' # cria o arquivo já na pasta em questão

# arquivo = open(caminho_arquivo, 'w')
# mexer nele
# arquivo.close() sempre fechar

# O 'w' apaga o arquivo e executa o que for pedido dentro do with, já o 'a' escreve ao final sem apagar o arquivo
with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo: # with com open() já abre e fecha o arquivo / encoding='utf8' serve para que caracteres especiais sejam lidos
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('Lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())

# os.remove(caminho_arquivo) ou os.unlink(caminho_arquivo)
# os.rename(caminho_arquivo, 'aula116-2.txt')