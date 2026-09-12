from flask import Blueprint, flash, render_template, request, redirect, url_for
from database.bancoPrincipal import conectar_banco


index_bp = Blueprint("index", __name__)


@index_bp.route("/index")
def tela():
    return render_template("index.html")
