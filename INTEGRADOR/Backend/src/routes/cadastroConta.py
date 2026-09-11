from flask import Blueprint, flash, render_template, request, redirect, url_for
from database.bancoPrincipal import conectar_banco


cadastroConta_bp = Blueprint("cadastroConta", __name__)


@cadastroConta_bp.route("/cadastroConta")
def tela():
    return render_template("cadastroConta.html")


@cadastroConta_bp.route("/cadastroConta.html", methods=["POST"])
def receber_dados():
    nome = request.form.get("nomeCadastroConta")
    senha = request.form.get("senhaCadastroConta")
    email = request.form.get("emailCadastroConta")
    telefone = request.form.get("telefoneCadastroConta")

    if not nome or not senha:
        flash("Preencha todos os campos.", "error")
        return redirect(url_for("cadastroConta.tela"))

    if senha != request.form.get("confirmarSenhaCadastroConta"):
        flash("As senhas não coincidem.", "error")
        return redirect(url_for("cadastroConta.tela"))

    conexao = None
    cursor = None

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO cadastroConta (nome, senha, email, telefone)
            VALUES (%s, %s, %s, %s)
        """

        flash("Usuario Cadastrado com sucesso!", "success")
        cursor.execute(sql, (nome, senha, email, telefone))
        conexao.commit()

        return redirect(url_for("cadastroConta.tela"))

    except Exception as erro:
        if conexao:
            conexao.rollback()

        print(f"🔴 ERRO NO BANCO DE DADOS: {erro}")
        
        flash("Erro ao salvar os dados.", "error")
        return redirect(url_for("cadastroConta.tela"))

        
    
    finally:
        if cursor:
            cursor.close()

        if conexao and conexao.is_connected():
            conexao.close()
