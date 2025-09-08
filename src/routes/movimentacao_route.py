from flask import request
from flask_restx import Namespace, Resource, fields

from src.service.movimentacao_service import MovimentacaoService

ns = Namespace('movimentacoes', description='Histórico de movimentações')

mov_model = ns.model('Movimentacoes', {
    'id': fields.Integer(readonly=True, description='Id da movimentacao'),
    'produto_id': fields.Integer(required=True, description='Id do produto a ser movimentado'),
    'tipo': fields.String(required=True, description='Tipo da movimentação: entrada | saida'),
    'quantidade': fields.Integer(required=True, description='Quantidade de itens a ser movimentado'),
    'data': fields.DateTime(readonly=True, description='Data da movimentacao'),
})

@ns.route('/')
class MovimentacaoList(Resource):
    @ns.marshal_list_with(mov_model)
    def get(self):
        return MovimentacaoService.listar_movimentacoes()
    @ns.expect(mov_model, validate=True)
    def post(self):
        try:
            mov = MovimentacaoService.movimentacao(request.json)
            return mov, 201
        except ValueError as e:
            return {'message': str(e)}, 400