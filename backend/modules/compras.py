from ..extensions import db

class OrdemCompra(db.Model):
    __tablename__ = 'ordens_compra'
    id = db.Column(db.Integer, primary_key=True)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedores.id'))

class NotaEntrada(db.Model):
    __tablename__ = 'notas_entrada'
    id = db.Column(db.Integer, primary_key=True)
    ordem_id = db.Column(db.Integer, db.ForeignKey('ordens_compra.id'))