from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

selecionar_grupo = 'SELECT id FROM grupos WHERE descricao = %s'
atualizar_contato = 'UPDATE contatos SET grupo_id = %s where nome = %s'

contato_grupo = {
    'Hanna': 'Casa',
    'Ana': 'Trabalho',
    'Bia': 'Trabalho',
    'Luca': 'Casa',
    'Lu': 'Casa',
    'Gui': 'Casa',
    'Beca': 'Trabalho',
    'Pedro': 'Trabalho',
}

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()

        for contato, grupo in contato_grupo.items():
            cursor.execute(selecionar_grupo, (grupo,))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(atualizar_contato, (grupo_id, contato))
            conexao.commit()

    except ProgrammingError as e:
        print(f'ERRO: {e.msg}')
    
    else:
        print('Contatos associados')