from database.bancoPrincipal import conectar_banco

def verificar_cadastro(email, senha):
    conexao = conectar_banco()
    
    if conexao is None: # Verifica se a conexão falhou
        return False, "Erro de conexão com o banco."
        print("🚨 [ERRO FATAL] falha ao conectar com o MySQL. Retornou None.")
        return False, "Sistema indisponível no momento. Tente novamente mais tarde."
    
    try:
        cursor = conexao.cursor(dictionary=True) # Cria um "cursor" — o objeto que efetivamente manda comandos SQL e lê respostas.
        # Dictionary = quando buscar resultados, me devolva cada linha como um dicionário Python
        
        # Monta o comando SQL e manda o cursor executá-lo, buscando um usuário cujo email bata com o texto digitado.
        query = "SELECT * FROM cadastroconta WHERE email = %s"
    
        cursor.execute(query, (email,)) 
        resultado = cursor.fetchone() 


        mensagem_erro = "Email ou senha não cadastrado." # Mensagem padrão de erro

        # 2. Verifica se achou algum usuário com esse email/nome
        if not resultado:
            return False, mensagem_erro # Retorna erro de email
        
        # 3. Se o usuário existe, vamos verificar se a senha bate
        if resultado['senha'] == senha:
            
            return True, resultado # Sucesso!
        else:
            return False, mensagem_erro # Retorna erro de senha

    except Exception as e:
        print(f"🚨 [ERRO NO BANCO] Falha ao executar a query: {e}")   
        return False, "Ocorreu um erro interno. Nossa equipe já foi notificada."

    finally: 
        if 'cursor' in locals():
            cursor.close()
        if conexao.is_connected():
            conexao.close()