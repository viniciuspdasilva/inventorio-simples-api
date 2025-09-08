from datetime import datetime
from enum import Enum

from src import db


class StatusPedido(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3


class Pedido(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(80), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(
        db.Enum(StatusPedido),
        nullable=False,
        default=1
    )
    criado_em = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.now
    )
    aprovado_em = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.now
    )

    produto_id = db.Column(
        db.Integer,
        db.ForeignKey('produtos.id'),
        nullable=False
    )
    fornecedor_id = db.Column(
        db.Integer,
        db.ForeignKey('fornecedores.id'),
        nullable=False
    )

    produto = db.relationship(
        'Produto',
        backref='pedidos',
        lazy='joined'
    )

    fornecedor = db.relationship(
        'Fornecedor',
        backref='pedidos',
        lazy='joined'
    )

    def __init__(self, nome, fornecedor_id, produtos_id, quantidade, status):
        self.descricao = nome
        self.fornecedor_id = fornecedor_id
        self.produtos_id = produtos_id
        self.quantidade = quantidade
        self.status = status

    def __repr__(self):
        return f"<Pedido id={self.id} nome={self.descricao} status={self.status.name}>"


class FornecedorProduto(db.Model):
    __tablename__ = 'fornecedor_produtos'

    fornecedor_id = db.Column(
        db.Integer,
        db.ForeignKey('fornecedores.id'),
        primary_key=True
    )
    produto_id = db.Column(
        db.Integer,
        db.ForeignKey('produtos.id'),
        primary_key=True
    )
