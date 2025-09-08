from src import db
from src.persistence.dao.movimentacoes_dao import MovimentacoesDAO
from src.persistence.dao.product_dao import ProductDAO


class MovimentacaoService:
    @staticmethod
    def listar_movimentacoes():
        return MovimentacoesDAO.get_all()

    @staticmethod
    def movimentacao(data):
        p = ProductDAO.get_by_id(data['produto_id'])
        if not p:
            raise ValueError('Product not found')
        if data['tipo'] == 'entrada':
            p.estoque += data['quantidade']
        elif data['tipo'] == 'saida':
            if p.estoque < data['quantidade']:
                raise ValueError('Quantidade insuficiente')
            p.estoque -= data['quantidade']
        else:
            raise ValueError('Tipo invalido')
        mov = MovimentacoesDAO.create(
            product_id=data['produto_id'],
            tipo=data['tipo'],
            quantidade=data['quantidade'],
            data=data['data']
        )
        db.session.commit()
        return mov
