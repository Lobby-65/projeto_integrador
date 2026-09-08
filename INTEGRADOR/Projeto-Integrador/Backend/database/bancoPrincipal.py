import mysql.connector

def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="senha",  # 0713
            database="projeto_grp"
        )
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None