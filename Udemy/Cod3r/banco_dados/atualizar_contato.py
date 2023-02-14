from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = 'UPDATE contatos set nome = %s WHERE id = %s'
args = (input('Digite o NOME de atualização: '), input('Digite o ID que deseja atualizar: '))

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()

    except ProgrammingError as e:
        print(f'Erro: {e.msg}')

    else:
        print(f'{cursor.rowcount} registro(s) atualizados(s).')
