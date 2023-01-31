from bd import nova_conexao
from mysql.connector import ProgrammingError

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute('DROP TABLE emails')
    except ProgrammingError as e:
        print(f'ERRO: {e.msg}')