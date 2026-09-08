from flask import Blueprint, flash, render_template, request, redirect, url_for
from database.bancoPrincipal import conectar_banco


login_bp = Blueprint("login", __name__)


@login_bp.route("/login")
def tela():
    return render_template("login.html")



@login_bp.route("/login", methods=["POST"])
def receber_dados():
    id = request.form.get("idLogin")
    senha = request.form.get("senhaLogin")

    if not id or not senha:
        flash("Preencha todos os campos.", "error")
        return redirect(url_for("login.tela"))
    
    conexao = None
    cursor = None

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO login (id, senha)
            VALUES (%s, %s)
        """

        flash("Usuario Conectado com sucesso!", "success")
        cursor.execute(sql, (id, senha))
        conexao.commit()

        return redirect(url_for("login.tela"))

    except Exception as erro:
        if conexao:
            conexao.rollback()

        print(f"🔴 ERRO NO BANCO DE DADOS: {erro}")
        
        flash("Erro ao salvar os dados.", "error")
        return redirect(url_for("login.tela"))

        
    
    finally:
        if cursor:
            cursor.close()

        if conexao and conexao.is_connected():
            conexao.close()
