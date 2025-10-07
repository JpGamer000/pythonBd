from mysql.connector import (connection)
from mysql.connector import errorcode
import os
from dotenv import load_dotenv

load_dotenv()
senha_bd = os.getenv('SENHA_SQL')

conexao_bd = connection.MySQLConnection()

conexao_bd = connection.MySQLConnection(
    host='localhost',
    user ='root',
    password = senha_bd,
    database = 'bd_python'
)

comando =  conexao_bd.cursor()
print(type(comando))
comando.execute("SELECT * FROM ALUNOS")
resultados = comando.fetchall()
print(resultados)

comando.close()
conexao_bd.close()