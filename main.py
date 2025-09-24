from mysql.connector import (connection)
from mysql.connector import errorcode

bd_conexao = connection.MySQLConnection(
    host='localhost',
    user='root',
    password='root',
    database='bd_python'
)