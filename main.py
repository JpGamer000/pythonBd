from mysql.connector import (connection)
from mysql.connector import errorcode
import os
from load_dotenv import load_dotenv

load_dotenv()
senha = os.getenv('senha_sql')

try:
    bd_conexao = connection.MySQLConnection(
        host='localhost',
        user='root',
        password=senha,
        database='bd_python'
    )
    print("Conexão bem sucedida!")

