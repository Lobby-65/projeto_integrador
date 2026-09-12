from flask import Blueprint, flash, render_template, request, redirect, url_for, session
from controllers.verificar_cadastro import verificar_cadastro


login_bp = Blueprint("login", __name__)


@login_bp.route("/login")
def tela():
    return render_template("login.html")



@login_bp.route("/login", methods=["GET", "POST"])
def receber_dados():

    if request.method == 'POST':
            # 1. Pega os dados do HTML (lembre-se: name="idLogin" e name="senhaLogin")
            email = request.form.get('emailLogin')
            senha = request.form.get('senhaLogin')
    
            # Se for None, significa que o usuário mandou o form vazio
            if not email or not senha:
                return render_template('login.html', erro="Preencha todos os campos.")
    
            session['usuario'] = email  # Armazena o usuário na sessão
            # 2. Chama a função de verificar, não de inserir!
            # Desempacotamento de Tupla.
            sucesso, resultado = verificar_cadastro(email, senha)
    
            # 3. Redireciona com base no resultado
            if sucesso:
                # redirect para a rota telaHome
                session['usuario'] = resultado['nome'] 
                return redirect(url_for('telaHome')) 
            else:
                return render_template('login.html', erro=resultado);
