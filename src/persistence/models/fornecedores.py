from src.database import db

class Fornecedores(db.Model):
    __tablename__ = 'fornecedores'
    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(14), nullable=False)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    telefone = db.Column(db.String, nullable=False)

    produtos = db.relationship(
        'produtos',
        secondary='fornecedor_produto',
        back_populates='fornecedores',
        lazy='dynamic'
    )

    def __init__(self, nome, email, telefone, cnpj):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cnpj = cnpj



class FornecedorProduto(db.Model):
    __tablename__ = 'fornecedor_produto'
    fornecedor_id = db.Column(
        db.Integer, db.ForeignKey('fornecedores.id'), primary_key=True
    )
    produto_id = db.Column(
        db.Integer, db.ForeignKey('produtos.id'), primary_key=True
    )