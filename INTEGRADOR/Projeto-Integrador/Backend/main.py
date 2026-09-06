from flask import Flask, render_template, request
from Backend.src.routes.login import login_bp
from Backend.src.routes.cadastroConta import cadastroConta_bp
from Backend.src.routes.index import index_bp

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
app.register_blueprint(login_bp)
app.register_blueprint(index_bp)
app.register_blueprint(cadastroConta_bp)


#ROTAS ENTRE INTERFACES
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastroConta')
def cadastroConta():
    return render_template('cadastroConta.html')


if __name__ == '__main__':
    app.run(debug=True)