from flask_restx import Namespace, Resource, fields

from src.routes.fornecedor_route import fornecedor_model
from src.service.pedido_service import PedidoService
from src.service.product_service import ProductService

ns = Namespace('pedidos_compra', description='Pedidos de compra')

pedido_model = ns.model('Pedidos', {
    'id':            fields.Integer(readonly=True),
    'nome':          fields.String(readonly=True),
    'produto_id':    fields.Integer(required=True),
    'fornecedor_id': fields.Integer(required=True),
    'quantidade':    fields.Integer(required=True),
    'status':        fields.String,
    'criado_em':     fields.DateTime,
})

@ns.route('')
class PedidoList(Resource):
    @ns.marshal_list_with(pedido_model)
    def get(self):
        return PedidoService.listar_pedidos()

@ns.route('/<int:id>')
class PedidoItem(Resource):
    @ns.marshal_with(pedido_model)
    def get(self, pid):
        try:
            return PedidoService.buscar_pedido(pid)
        except ValueError as e:
            ns.abort(404, str(e))


@ns.route('/<int:id>/fornecedor')
class PedidoFornecedorItem(Resource):
    @ns.marshal_list_with(fornecedor_model)
    def get(self, pid):
        p = ProductService.get_product_by_id(pid)
        return p.fornecedores
@ns.route('/<int:id>/repor')
class ProdutoRepor(Resource):
    @ns.marshal_list_with(pedido_model)
    def get(self, pid):
        pedido = ProductService.verificar_estoque_e_repor(pid)
        if not pedido:
            ns.abort(404, str('Estoque ainda não zerado'))
        return pedido