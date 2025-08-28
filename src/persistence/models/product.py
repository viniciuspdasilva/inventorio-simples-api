from src.database import db


class Product(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)
    is_critical = db.Column(db.Boolean, nullable=False, default=False)
    movimentacoes = db.relationship('Movimentacoes', backref='produto', lazy='joined')
    estoque_minimo = db.Column(db.Integer, nullable=False, default=0)
    fornecedores = db.relationship(
        'Fornecedor',
        secondary='fornecedor_produto',
        back_populates='produtos',
        lazy='joined'
    )

    def __init__(self, name, description, price, estoque, is_critical = False):
        self.name = name
        self.description = description
        self.price = price
        self.estoque = estoque
        self.is_critical = is_critical
