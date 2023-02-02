from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Ana', '98235-4321'),
    ('Bia', '97795-2413'),
    ('Luca', '98115-8321'),
    ('Lu', '92165-0321'),
    ('Gui', '99765-4301'),
    ('Beca', '98065-1021'),
    ('Pedro', '98761-8329'),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'ERRO: {e.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros!')
