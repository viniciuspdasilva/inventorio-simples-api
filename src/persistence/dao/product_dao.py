from src.persistence.models.product import Product
from src.database import db

class ProductDAO:
    @staticmethod
    def get_all():
        return Product.query.all()
    @staticmethod
    def get_by_id(pid):
        return Product.query.get(pid)
    @staticmethod
    def add(name, description, price, estoque=0):
        product = Product(name, description, price, estoque)
        db.session.add(product)
        db.session.commit()
        return product
    @staticmethod
    def delete(pid):
        product = Product.query.get(pid)
        if product:
            db.session.delete(product)
            db.session.commit()
        return product
