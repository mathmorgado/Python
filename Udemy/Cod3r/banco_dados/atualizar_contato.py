from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = 'UPDATE nome FROM contatos WHERE id = %s'
args = (input('Digite o ID para atualizar o nome: '),)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()

    except ProgrammingError as e:
        print(f'Erro: {e.msg}')

    else:
        print(f'{cursor.rowcount} registro(s) atualizados(s).')
