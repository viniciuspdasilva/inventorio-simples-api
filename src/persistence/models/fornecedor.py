from src.database import db

class Fornecedor(db.Model):
    __tablename__ = 'fornecedores'
    __table_args__ = (
        db.Index('ix_fornecedor_cnpj_email', 'cnpj', 'email'),
    )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cnpj = db.Column(db.String(14), nullable=False, unique=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    telefone = db.Column(db.String(20), nullable=False)

    produtos = db.relationship(
        'Produto',
        back_populates='fornecedor',
        lazy='dynamic'
    )

    def __init__(self, nome, email, telefone, cnpj):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cnpj = cnpj

    def __repr__(self):
        return f"<Fornecedor id={self.id} nome={self.nome} email={self.email} telefone={self.telefone}>"
