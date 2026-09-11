from flask import Flask, render_template, request, redirect, url_for, session
# from src.routes.login import login_bp
from src.routes.cadastroConta import cadastroConta_bp
from src.routes.index import index_bp
from src.routes.telaHome import telaHome_bp
from controllers.verificar_cadastro import verificar_cadastro

# O "../" faz o caminho voltar um diretório acima do Backend
app = Flask(__name__, template_folder="../front/templates",
    static_folder="../front/Static/CSS",
    static_url_path="/static")


app.secret_key = "ChaveSecreta"



# Define a rota base como a index
@app.route('/')
def index():
    return render_template('index.html') 

#BLUEPRINTS DE CADA INTERFACE
# app.register_blueprint(login_bp)
app.register_blueprint(index_bp)
app.register_blueprint(cadastroConta_bp)
app.register_blueprint(telaHome_bp)


# #ROTAS ENTRE INTERFACES
# @app.route('/login')
# def login():
#     return render_template('login.html')

@app.route('/cadastroConta')
def cadastroConta():
    return render_template('cadastroConta.html')

@app.route('/telaHome')
def telaHome():
    return render_template('telaHome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 1. Pega os dados do HTML (lembre-se: name="idLogin" e name="senhaLogin")
        usuario_digitado = request.form.get('idLogin')
        senha_digitada = request.form.get('senhaLogin')

        # Se for None, significa que o usuário mandou o form vazio
        if not usuario_digitado or not senha_digitada:
            return render_template('login.html', erro="Preencha todos os campos.")

        session['usuario'] = usuario_digitado  # Armazena o usuário na sessão
        # 2. Chama a função de verificar, não de inserir!
        # Desempacotamento de Tupla.
        sucesso, resultado = verificar_cadastro(usuario_digitado, senha_digitada)

        # 3. Redireciona com base no resultado
        if sucesso:
            # redirect para a rota telaHome
            session['usuario'] = resultado['nome'] 
            return redirect(url_for('telaHome')) 
        else:
            return render_template('login.html', erro=resultado)

    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)