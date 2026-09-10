from flask import Blueprint, flash, render_template, request, redirect, url_for, session
from database.bancoPrincipal import conectar_banco


telaHome_bp = Blueprint("telaHome", __name__)


@telaHome_bp.route("/telaHome")
def tela():
    if 'usuario' in session:
        usuario_logado = session['usuario']
    return render_template("telaHome.html", usuario=usuario_logado)

    return redirect(url_for('login'))  # Redireciona para a página de login se o usuário não estiver logado
