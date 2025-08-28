from src.persistence.dao.pedido_dao import PedidoDAO


class PedidoService:
    @staticmethod
    def listar_pedidos():
        return PedidoDAO.get_all_pedidos()
    @staticmethod
    def buscar_pedido(pid):
        pedido = PedidoDAO.get_pedido_per_id(pid)
        if not pedido:
            raise ValueError("Pedido não encontrado")
        return pedido
    @staticmethod
    def criar_pedido(data):
        return PedidoDAO.create_pedido(**data)