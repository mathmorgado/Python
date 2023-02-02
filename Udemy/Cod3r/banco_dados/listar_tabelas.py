from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute('SHOW TABLES')

        for i, tables in enumerate(cursor, start=1):
            print(f'Tabela {i} - {tables[0]}')
    except ProgrammingError as e:
        print(f'ERRO? {e.msg}')