from flask import Blueprint, jsonify

estoque_bp = Blueprint('estoque_bp', __name__, url_prefix='/estoque')

@estoque_bp.route('/itens')
def list_itens():
    return jsonify({'message': 'Lista de itens do estoque'})