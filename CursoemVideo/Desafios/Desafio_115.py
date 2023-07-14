from Pacotes.Desafio_115.Sistema.Modulos_Sistema import Cadastros
from Pacotes.Desafio_115.Arquivo.Modulos_Arquivo \
    import ArquivoExiste, CriarArquivo

arq = 'Pessoas.txt'

if not ArquivoExiste(arq):
    CriarArquivo('Pessoas.txt')

Cadastros('\033[92mOpção desejada:\033[m ')
