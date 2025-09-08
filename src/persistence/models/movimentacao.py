import enum
from datetime import datetime
from src.database import db

class TipoMovimentacao(enum.Enum):
    ENTRADA = 'entrada'
    SAIDA = 'saida'

class Movimentacao(db.Model):
    __tablename__ = 'movimentacoes'
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(
        db.Integer,
        db.ForeignKey('produtos.id'),
        nullable=False
    )
    tipo = db.Column(db.Enum(TipoMovimentacao), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    data = db.Column(db.DateTime, nullable=False, default=datetime.now)

    produto = db.relationship(
        'Produto',
        back_populates='movimentacoes',
        lazy='joined'
    )

    def __repr__(self):
        return f"<Movimentacao {self.id} – {self.tipo}:{self.quantidade}>"

    def __init__(self, product_id, tipo, quantidade, data):
        self.produto_id = product_id
        self.tipo = tipo
        self.quantidade = quantidade
        self.data = data







