from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Cliente
from .. import db

cadastros_bp = Blueprint('cadastros_bp', __name__, url_prefix='/cadastros')

@cadastros_bp.route('/clientes')
def list_clientes():
    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes)

@cadastros_bp.route('/clientes/add', methods=['POST'])
def add_cliente():
    nome = request.form.get('nome')
    if nome:
        cliente = Cliente(nome=nome)
        db.session.add(cliente)
        db.session.commit()
    return redirect(url_for('cadastros_bp.list_clientes'))