from ..extensions import db

class Estoque(db.Model):
    __tablename__ = 'estoques'
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)

class Inventario(db.Model):
    __tablename__ = 'inventarios'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)

class MovimentoEstoque(db.Model):
    __tablename__ = 'movimentos_estoque'
    id = db.Column(db.Integer, primary_key=True)
    estoque_id = db.Column(db.Integer, db.ForeignKey('estoques.id'), nullable=False)
    tipo = db.Column(db.String(10), nullable=False)  # entrada ou saida
    quantidade = db.Column(db.Integer, nullable=False)