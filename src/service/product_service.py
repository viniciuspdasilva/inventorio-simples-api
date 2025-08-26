from src.persistence.dao.product_dao import ProductDAO


class ProductService:
    @staticmethod
    def list_all_products():
        return ProductDAO.get_all()

    @staticmethod
    def get_product_by_id(product_id):
        p = ProductDAO.get_by_id(product_id)
        if not p:
            raise ValueError("Product not found")
        return p

    @staticmethod
    def create_product(product):
        return ProductDAO.add(
            name=product["name"],
            price=product["price"],
            description=product["description"],
            estoque=product.get("estoque", 0),
        )

    @staticmethod
    def remove_product(product_id):
        p = ProductDAO.delete(product_id)
        if not p:
            raise ValueError("Product not found")
        return p