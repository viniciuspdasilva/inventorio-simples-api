from datetime import datetime

from src import db


class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedores.id'), nullable=False)
    produtos_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=1)
    criado_em = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    aprovado_em = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    produto = db.relationship('Produto')
    fornecedor = db.relationship('Fornecedores')

    def __init__(self, nome, fornecedor_id, produtos_id, quantidade, status):
        self.nome = nome
        self.fornecedor_id = fornecedor_id
        self.produtos_id = produtos_id
        self.quantidade = quantidade
        self.status = status