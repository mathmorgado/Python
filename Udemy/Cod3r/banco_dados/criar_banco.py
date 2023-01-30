from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='2512'
)

cursor = conexao.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS agenda')