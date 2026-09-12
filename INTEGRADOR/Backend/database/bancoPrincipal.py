import mysql.connector

def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="0713",
            database="projeto_grp"
        )
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cadastroConta (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(15) NOT NULL,
                senha VARCHAR(15) NOT NULL,
                email VARCHAR(15) NOT NULL,
                telefone VARCHAR(15) NOT NULL
            )
        """)
        conexao.commit()
        cursor.close()

        return conexao

    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None