from src.database import db


class Produto(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False, default=0)
    estoque = db.Column(db.Integer, nullable=False, default=0)
    is_critical = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )
    estoque_minimo = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    movimentacoes = db.relationship(
        'Movimentacao',
        backref='produtos_movimentacoes',
        lazy='dynamic'
    )

    fornecedor_id = db.Column(
        db.Integer,
        db.ForeignKey('fornecedores.id'),
        nullable=False
    )

    fornecedor = db.relationship(
        'Fornecedor',
        back_populates='produtos',
        lazy='joined'
    )

    def __init__(self, name, description, price, estoque, is_critical=False):
        self.name = name
        self.description = description
        self.price = price
        self.estoque = estoque
        self.is_critical = is_critical
