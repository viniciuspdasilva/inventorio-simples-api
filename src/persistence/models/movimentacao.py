from datetime import datetime
from src.database import db

class Movimentacao(db.Model):
    __tablename__ = 'movimentacao'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
    tipo = db.Column(db.String(10), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)

    product = db.relationship('produtos', backref='movimentacoes')

    def __init__(self, product_id, tipo, quantidade, data):
        self.product_id = product_id
        self.tipo = tipo
        self.quantidade = quantidade
        self.data = data







