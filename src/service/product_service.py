from src.enum.status_pedido import PedidoStatus
from src.persistence.dao.product_dao import ProductDAO
from src.persistence.models.product import Product
from src.service.pedido_service import PedidoService
import uuid

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
    @staticmethod
    def verificar_estoque_e_repor(pid_produto):
        product = ProductDAO.get_by_id(pid_produto)
        if not product:
            raise ValueError("Product não encontrado")
        novo_pedido = ProductService.__logica_verificar_estoque_e_repor(product)
        if novo_pedido is not None:
            PedidoService.criar_pedido(novo_pedido)
        return novo_pedido

    @staticmethod
    def __logica_verificar_estoque_e_repor(produto: Product):
        if produto.estoque < 0 and produto.fornecedores:
            fornecedor = produto.fornecedores[0]
            pedido = PedidoService.criar_pedido({
                "nome": produto.nome + "-" + fornecedor.nome + "-" + uuid.uuid4(),
                "fornecedor_id": fornecedor.id,
                "produtos_id": produto.id,
                "quantidade": produto.estoque_minimo or 5,
                "status": PedidoStatus.INITIALIZED.value,
            })
            return pedido
        return None
