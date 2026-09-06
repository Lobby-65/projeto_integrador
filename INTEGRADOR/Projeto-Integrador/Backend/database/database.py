import mysql.connector

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="0713",
        database="projeto_grp"
    )