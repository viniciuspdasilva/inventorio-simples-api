from src.database import db
from src.persistence.models.movimentacao import Movimentacao


class MovimentacoesDAO:
    @staticmethod
    def get_all():
        return Movimentacao.query.order_by(Movimentacao.data.desc()).all()
    @staticmethod
    def create(product_id, tipo, quantidade, data):
        movimentacao = Movimentacao(
            product_id=product_id,
            tipo=tipo,
            quantidade=quantidade,
            data=data
        )
        db.session.add(movimentacao)
        return movimentacao