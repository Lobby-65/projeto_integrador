from flask import Blueprint, flash, render_template, request, redirect, url_for
from database.database import conectar_banco


login_bp = Blueprint("login", __name__)


@login_bp.route("/")
def tela():
    return render_template("cadastroConta.html")


@login_bp.route("/login", methods=["POST"])
def receber_dados():
    nome = request.form.get("nomeCadastro")
    senha = request.form.get("senhaCadastro")
    email = request.form.get("emailCadastro")
    telefone = request.form.get("telefoneCadastro")

    if not nome or not senha:
        flash("Preencha todos os campos.", "error")
        return redirect(url_for("login.tela"))

    if senha != request.form.get("confirmarSenhaCadastro"):
        flash("As senhas não coincidem.", "error")
        return redirect(url_for("login.tela"))

    conexao = None
    cursor = None

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO login (nome, senha, email, telefone)
            VALUES (%s, %s, %s, %s)
        """

        flash("Usuario Cadastrado com sucesso!", "success")
        cursor.execute(sql, (nome, senha, email, telefone))
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
