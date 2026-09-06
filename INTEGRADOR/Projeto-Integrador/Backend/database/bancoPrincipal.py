import mysql.connector

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        #A SENHA DEPENDE A SUA SENHA PESSOAL DO MYSQL
        password="0713",
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        database="projeto_grp"
    )