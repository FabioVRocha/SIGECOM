from flask import Blueprint, jsonify

vendas_bp = Blueprint('vendas_bp', __name__, url_prefix='/vendas')

@vendas_bp.route('/')
def list_vendas():
    return jsonify({'message': 'Lista de vendas'})