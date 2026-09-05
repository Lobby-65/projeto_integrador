from flask import Flask, render_template, request
from src.routes.login import login_bp

# O "../" faz o caminho voltar um diretório acima do Backend
app = Flask(__name__, template_folder="../front/templates",
    static_folder="../front/Static/CSS",
    static_url_path="/static")


app.secret_key = "ChaveSecreta"

app.register_blueprint(login_bp)


if __name__ == '__main__':
    app.run(debug=True)