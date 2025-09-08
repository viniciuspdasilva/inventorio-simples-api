from src.persistence.models.produto import Produto
from src.database import db

class ProductDAO:
    @staticmethod
    def get_all():
        return Produto.query.all()
    @staticmethod
    def get_by_id(pid):
        return Produto.query.get(pid)
    @staticmethod
    def add(name, description, price, estoque=0):
        product = Produto(name, description, price, estoque)
        db.session.add(product)
        db.session.commit()
        return product
    @staticmethod
    def delete(pid):
        product = Produto.query.get(pid)
        if product:
            db.session.delete(product)
            db.session.commit()
        return product
