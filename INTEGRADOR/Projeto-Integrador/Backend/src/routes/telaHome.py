from flask import Blueprint, flash, render_template, request, redirect, url_for
from database.bancoPrincipal import conectar_banco


telaHome_bp = Blueprint("telaHome", __name__)


@telaHome_bp.route("/telaHome")
def tela():
    return render_template("telaHome.html")
