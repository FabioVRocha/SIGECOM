from ..extensions import db

class ContaPagar(db.Model):
    __tablename__ = 'contas_pagar'
    id = db.Column(db.Integer, primary_key=True)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedores.id'))
    valor = db.Column(db.Numeric(10, 2))

class ContaReceber(db.Model):
    __tablename__ = 'contas_receber'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    valor = db.Column(db.Numeric(10, 2))

class Caixa(db.Model):
    __tablename__ = 'caixa'
    id = db.Column(db.Integer, primary_key=True)
    saldo = db.Column(db.Numeric(10, 2))

class ConciliacaoBancaria(db.Model):
    __tablename__ = 'conciliacoes_bancarias'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)

class FormaPagamento(db.Model):
    __tablename__ = 'formas_pagamento'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(50))