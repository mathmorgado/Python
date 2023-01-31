from mysql.connector import connect
from contextlib import contextmanager

informacoes = dict(
    host='localhost',
    port=3306,
    user='root',
    passwd='2512',
    database='agenda'
)

@contextmanager
def nova_conexao():
    conexao = connect(**informacoes)
    try:
        yield conexao
    finally:
        if (conexao and conexao.is_connected()):
            conexao.close()

