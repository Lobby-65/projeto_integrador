from database.bancoPrincipal import conectar_banco

def verificar_cadastro(nome, senha):
    conexao = conectar_banco()
    
    if conexao is None:
        return False, "Erro de conexão com o banco."
    
    try:
        cursor = conexao.cursor(dictionary=True) 
        
        # 1. Busca APENAS pelo nome ou email (Tiramos o AND senha = %s daqui)
        query = "SELECT * FROM cadastroconta WHERE nome = %s OR email = %s"
        cursor.execute(query, (nome, nome)) 
        resultado = cursor.fetchone() 

        # 2. Verifica se achou algum usuário com esse email/nome
        if not resultado:
            return False, "Email ou ID não cadastrado." # Retorna erro de email
        
        # 3. Se o usuário existe, vamos verificar se a senha bate
        if resultado['senha'] == senha:
            return True, resultado # Sucesso!
        else:
            return False, "Senha incorreta." # Retorna erro de senha

    except Exception as e:
        return False, f"Erro ao consultar o banco de dados: {e}" 

    finally: 
        if 'cursor' in locals():
            cursor.close()
        if conexao.is_connected():
            conexao.close()