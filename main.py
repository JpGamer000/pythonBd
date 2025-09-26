from mysql.connector import (connection)
from mysql.connector import errorcode
import os
from dotenv import load_dotenv

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
except mysql.connector.Error as erro:  # Corrigido: adicionado 'mysql.connector' antes do Error
    if erro.errno == errorcode.ER_BAD_DB_ERROR:
        print("O banco de dados não existe!")
    elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Usuário ou senha incorretos!")
    else:
        print(erro)
        
comando = bd_conexao.cursor()
select = comando.execute("SELECT * FROM ALUNOS")
resultado = comando.fetchall()
for linha in resultado:
   print(linha)

sql_insert = "INSERT INTO ALUNOS (nome, ano) VALUES (%s, %s)"
valores1 = ('Caio', '3 TEC')  
valores2 = ('Bernardo', '3 TEC') 

comando.execute(sql_insert, valores1)
comando.execute(sql_insert, valores2)

print("==TEST INSERT==")
select = comando.execute("SELECT * FROM ALUNOS")
resultado = comando.fetchall()
for linha in resultado:
   print(linha)

comando.close()
bd_conexao.commit()
bd_conexao.close