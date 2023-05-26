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
with open(caminho_arquivo, 'w') as arquivo: # with com open() já abre e fecha o arquivo
    print('Olá mundo')
    print('Arquivo vai ser fechado')