from src import db
from src.persistence.dao.fornecedor_dao import FornecedorDAO
from src.persistence.dao.product_dao import ProductDAO
from src.persistence.models.pedido import Pedido

class PedidoDAO:
    @staticmethod
    def get_all_pedidos():
        return Pedido.query.order_by(Pedido.criado_em.desc()).all()
    @staticmethod
    def get_pedido_per_id(pid):
        return Pedido.query.get(pid)
    @staticmethod
    def create_pedido(nome, fornecedor_id, produtos_id, quantidade, status):
        produto = ProductDAO.get_by_id(produtos_id)
        if produto is None:
            raise TypeError("Produto não encontrado")
        fornecedor = FornecedorDAO.get_fornecedor_by_id(fornecedor_id)
        if not fornecedor:
            raise TypeError("Fornecedor não encontrado")
        p = Pedido(nome, fornecedor_id, produtos_id, quantidade, status)
        db.session.add(p)
        db.session.commit()
        return p